import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import visualisation_toolkit.chart_format_config as cfc

co2_emission_df = pd.read_csv('./our_world_in_data/data_source/annual-co2-emissions-per-country.csv')
co2_emission_df.columns
co2_emission_df.groupby(by = 'Entity').sum().sort_values(by = 'Annual CO₂ emissions (tonnes)', ascending = False).head(50)
monitor_list = ['Africa','Asia (excl. China & India)','China', 'EU-28', 'Europe (excl. EU-28)','North America (excl. USA)','India','Oceania','South America','United States']

co2_emission_by_selected_region = co2_emission_df[co2_emission_df['Entity'].isin(monitor_list)]
co2_emission_by_selected_region_after_1900 = co2_emission_by_selected_region[co2_emission_by_selected_region['Year'] >= 1900]


monitor_list_sorted = co2_emission_by_selected_region_after_1900.groupby(by = 'Entity').sum().sort_values(by = 'Annual CO₂ emissions (tonnes)', ascending = False).index
monitor_list_sorted

region_color_dict = {
    'United States' : '65,105,225',
    'EU-28' : '127,255,212',
    'Asia (excl. China & India)' : '144,238,144',
    'China' : '240,230,140',
    'Europe (excl. EU-28)' : '255,160,122',
    'North America (excl. USA)' : '255,127,80',
    'India' : '219,112,147',
    'Africa' : '186,85,211',
    'South America' : '147,112,219',
    'Oceania' : '128,0,128'
}

fig = go.Figure()
cfc.configure_chart(fig)

for region in monitor_list_sorted:
    ind_region_df = co2_emission_by_selected_region_after_1900[co2_emission_by_selected_region_after_1900['Entity'] ==  region]
    fig.add_trace(
        go.Scatter(
            name = region,
            x = ind_region_df['Year'],
            y = ind_region_df['Annual CO₂ emissions (tonnes)'],
            mode='lines',
            line = dict(
                shape = 'spline',
                width = 1,
                color = 'rgb('+region_color_dict[region]+')',
            ),
            fillcolor = 'rgba('+region_color_dict[region]+',0.7)',
            stackgroup = 'emmission',
        )
    )

fig.update_layout(
    showlegend= False,
    xaxis=dict(
        type='linear',
        range=[1900, 2020],
        )
)
fig.show()
fig.to_image(engine = 'kaleido')
fig.write_image('./our_world_in_data//data_processed/co2_emission_evolution_by_countries.svg')
