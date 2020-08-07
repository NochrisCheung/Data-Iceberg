import pandas as pd
import plotly.graph_objects as go
import visualisation_toolkit.chart_format_config as cfc
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
import numpy as np

food_balance_df = pd.read_csv('./faostat/data_source/FoodBalanceSheets_E_All_Data.csv', encoding = 'ISO-8859-1')
food_balance_by_country = food_balance_df.groupby(by = ['Area', 'Item', 'Element','Unit']).sum()['Y2017'].reset_index()

protein_bool = [True if 'Protein' in v else False for v in food_balance_by_country['Element'].values]
fat_bool = [True if 'Fat' in v else False for v in food_balance_by_country['Element'].values]

protein_gram_by_countries = food_balance_by_country[protein_bool].groupby(by = ['Area','Element']).sum().reset_index()
protein_gram_by_countries['protein_kcal'] = protein_gram_by_countries['Y2017'].mul(4)

fat_gram_by_countries = food_balance_by_country[fat_bool].groupby(by = ['Area','Element']).sum().reset_index()
fat_gram_by_countries['fat_kcal'] = fat_gram_by_countries['Y2017'].mul(9)

food_supply_kcal_by_countries = food_balance_by_country[food_balance_by_country['Element'] == 'Food supply (kcal/capita/day)'].groupby(by = ['Area','Element']).sum().reset_index()
protein_and_fat_gram_by_countries = protein_gram_by_countries.merge(fat_gram_by_countries, how = 'inner', on = ['Area'])
all_data_by_countries = protein_and_fat_gram_by_countries.merge(food_supply_kcal_by_countries, how = 'inner', on = ['Area'])

all_kcal_by_countries = all_data_by_countries[['Area', 'protein_kcal','fat_kcal','Y2017']]
all_kcal_by_countries.columns = ['Countries','Kcal from Protein', 'Kcal from Fat','Kcal from All Food']
all_kcal_by_countries['Kcal from Carbohydrates'] = all_kcal_by_countries['Kcal from All Food'] - all_kcal_by_countries['Kcal from Protein'] - all_kcal_by_countries['Kcal from Fat']
all_kcal_by_countries
not_include_list = [
    'Australia and New Zealand',
    'Asia',
    'Americas',
    'Africa',
    'China',
    'Central America',
    'Central Asia',
    'Eastern Africa',
    'Eastern Asia',
    'Eastern Europe',
    'Europe',
    'Least Developed Countries',
    'Low Income Food Deficit Countries',
    'Middle Africa',
    'Net Food Importing Developing Countries',
    'Northern Africa',
    'Northern America',
    'Northern Europe',
    'Oceania',
    'Small Island Developing States',
    'South America',
    'South-Eastern Asia',
    'Southern Africa',
    'Southern Asia',
    'Southern Europe',
    'Western Africa',
    'Western Asia',
    'Western Europe',
    'World',
    'European Union',
    'Land Locked Developing Countries',
    ]

all_kcal_by_countries_filtered  = all_kcal_by_countries[~all_kcal_by_countries['Countries'].isin(not_include_list)].reset_index(drop = True)
all_kcal_by_countries_filtered['Protein %'] = all_kcal_by_countries_filtered['Kcal from Protein']/all_kcal_by_countries_filtered['Kcal from All Food']
all_kcal_by_countries_filtered['Carbohydrates %'] = all_kcal_by_countries_filtered['Kcal from Carbohydrates']/all_kcal_by_countries_filtered['Kcal from All Food']
all_kcal_by_countries_filtered['Fat %'] = all_kcal_by_countries_filtered['Kcal from Fat']/all_kcal_by_countries_filtered['Kcal from All Food']
all_kcal_by_countries_filtered.sort_values(by = 'Fat %', ascending = False).tail(50)
all_kcal_by_countries_filtered.count()
all_kcal_by_countries_filtered[all_kcal_by_countries_filtered['Fat %'] <= 0.2].count()
# X = [[c, p, f] for c, p, f in zip(all_kcal_by_countries_filtered['Carbohydrates %'].values, all_kcal_by_countries_filtered['Protein %'].values, all_kcal_by_countries_filtered['Fat %'].values)]
# # X = [[c, p] for c, p in zip(all_kcal_by_countries_filtered['Carbohydrates %'].values, all_kcal_by_countries_filtered['Protein %'].values)]
# # X = all_kcal_by_countries_filtered['Carbohydrates %'].values
# y = all_kcal_by_countries_filtered['Fat %'].values
#  X = np.array([[c, p, f] for c, p, f in zip(all_kcal_by_countries_filtered['Carbohydrates %'].values, all_kcal_by_countries_filtered['Protein %'].values, all_kcal_by_countries_filtered['Fat %'].values)])
#  kmeans = KMeans(n_clusters = 2, random_state = 0 ).fit(X)
#  kmeans.labels_
#
#
# reg = LinearRegression().fit(X,y)
# reg.score(X, y)
# reg.intercept_
# reg.coef_

all_kcal_by_countries_filtered[all_kcal_by_countries_filtered['Countries'] == 'World']
population_by_countries = food_balance_df[(food_balance_df['Element'] == 'Total Population - Both sexes') & (~food_balance_df['Area'].isin(not_include_list))][['Area', 'Y2017']]
population_by_countries.columns = ['Countries', 'Population']
population_by_countries_matched = all_kcal_by_countries_filtered.merge(population_by_countries, how = 'inner', on = ['Countries'])
# population_by_countries_matched[['Countries','Population']].sort_values(by = 'Population', ascending = False).head(50)

fig = go.Figure()
cfc.configure_chart(fig)
fig.add_trace(
    go.Scatter(
        y = all_kcal_by_countries_filtered['Carbohydrates %'],
        x = all_kcal_by_countries_filtered['Protein %'],
        mode = 'markers+text',
        marker = dict(
            size = population_by_countries_matched['Population'].transform([np.sqrt]).div(25),
            color = all_kcal_by_countries_filtered['Fat %'],
             # + all_kcal_by_countries_filtered['Protein %'],
            opacity = 0.9,
            line_width = 0.5,
            line_color = '#2A3F5F',

            colorscale = 'Plasma',
            colorbar = dict(
                thickness = 10,
                lenmode = 'pixels',
                len = 420,
                dtick = 0.1,
                yanchor = 'middle',
                tickformat = '%',
            ),
        ),

        text = [c if p > 10000 else '' for c, p in zip(population_by_countries_matched['Countries'], population_by_countries_matched['Population'])],
        # text = [country if country in label_list else '' for country in all_kcal_by_countries_filtered['Countries']],
        textfont_size = 10,
    ),
)

fig.update_traces(textposition='middle right')

fig.update_layout(
    showlegend= False,
    xaxis=dict(
        showticklabels=True,
        zeroline = False,
        showgrid = False,
        dtick = 0.02,
        tickformat = '%',

        ticks = 'inside',
        tickwidth = 1,
        ticklen = 7,
        tickcolor='#2A3F5F',

        range = [0.08, 0.145]
        ),
    yaxis = dict(
        type = 'linear',
        showline = False,
        showgrid = False,
        zeroline = False,
        showticklabels = True,
        dtick = 0.1,
        tickformat = '%',

        ticks = 'inside',
        tickwidth = 1,
        ticklen = 7,
        tickcolor='#2A3F5F',

        range = [0.44, 0.81]
        ),
    # bargroupgap = 0
)

fig.update_layout(
    margin=dict(
        l=60,
        r=30,
        b=60,
        t=180,
        pad = 5
    )
)
fig.show()
fig.to_image(engine = 'kaleido')
fig.write_image('./faostat/data_processed/dietary_energy_share_by_countries.svg')
