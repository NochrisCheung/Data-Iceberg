import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import visualisation_toolkit.chart_format_config as cfc
dogs_df = pd.read_csv('./data_source/american_kennel_club/dog_breed_popularity_rank/Dog Breed Popularity - 2013.csv', names = ['Breed','2013'])
for i in range(2014,2020):
    # dogs_df['dog_pop_rank_'+str(i)] = pd.read_csv('./data_source/american_kennel_club/dog_breed_popularity_rank/Dog Breed Popularity - '+ str(i) +'.csv')
    print(i)
    dogs_df = dogs_df.merge(pd.read_csv('./data_source/american_kennel_club/dog_breed_popularity_rank/Dog Breed Popularity - '+ str(i) +'.csv', names = ['Breed',str(i)]), on ='Breed')
# for i in range(2014,2020):
#     all_dogs_ranks = all_dogs_ranks.merge(dogs_df['dog_pop_rank_'+str(i)], on = 'Breed')
dogs_df_ranked_by_2019.head(10)

dogs_df_ranked_by_2019 = dogs_df[1:].sort_values(by = '2019')
dogs_df_ranked_by_2019['Breed'] = dogs_df_ranked_by_2019['Breed'].astype('string')
for i in range(2013, 2020):
    dogs_df_ranked_by_2019[str(i)] = dogs_df_ranked_by_2019[str(i)].astype('int')

color_scheme = [
    '65,105,225',
    '127,255,212',
    '144,238,144',
    '240,230,140',
    '255,160,122',
    '205,92,92',
    '219,112,147',
    '186,85,211',
    '147,112,219',
    '33,33,33'
]

fig = make_subplots(specs=[[{"secondary_y": True}]])
cfc.configure_chart(fig)

for i in range (1, 11):
    ranked_dog_df = dogs_df_ranked_by_2019[dogs_df_ranked_by_2019['2019'] == i]
    [n] = ranked_dog_df['Breed']
    [rank] = ranked_dog_df.iloc[0:,1:].values
    fig.add_trace(
        go.Scatter(
            name = n,
            x = ranked_dog_df.iloc[0:,1:].columns,
            y = rank,
            mode = 'markers+lines',
            line = dict(
                width = 8,
                color = 'rgb('+color_scheme[i-1]+')'
            ),
            marker = dict(
                size = 8,
                # [30 if i == 10 else 10],
                color = 'rgb('+color_scheme[i-1]+')'
            )
        ),
        secondary_y = True
        # [True if i == 10 else False]
    )

fig.update_layout(
    showlegend = False,
    yaxis1 = dict(
        range = [0,0],
        showline = False,
        showgrid = False,
        zeroline = False,
    ),
    yaxis2 = dict(
        range = [10.5,0.5],
        dtick = 1,

        showline = False,
        showgrid = False,
        zeroline = False,
    )
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

fig.to_image(engine = 'kaleido')
fig.write_image('topics/011_dog_breed_popularity_ranking/data_processed/dog_breed_popularity_ranking.svg')
