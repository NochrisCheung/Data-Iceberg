import pandas as pd
import numpy as np
import plotly.graph_objects as go
import visualisation_toolkit.chart_format_config as cfc

energy_df = pd.read_csv('./data_source/our_world_in_data/energy_consumption/global-primary-energy.csv')
energy_df
energy_df_1950_afterward = energy_df[energy_df['Year']>=1950]
energy_df_1950_afterward = energy_df_1950_afterward.set_index('Year')
energy_df_1950_afterward.sum(axis = 1)
energy_df_1950_afterward = energy_df_1950_afterward.reindex(energy_df_1950_afterward.mean().sort_values(ascending = False).index, axis=1)
energy_df_1950_afterward
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

energy_df_1950_afterward.tail(1)/energy_df_1950_afterward.tail(1).sum().sum()

fig = cfc.configure_chart()
energy_df_1950_afterward.columns
c = 0
for source in energy_df_1950_afterward.columns:
    ind_source_df = energy_df_1950_afterward[source]
    fig.add_trace(
        go.Scatter(
            name = source,
            x = ind_source_df.index,
            y = ind_source_df.values,
            mode='lines',
            line = dict(
                shape = 'spline',
                width = 1,
                color = 'rgb('+color_scheme[c]+')',
            ),
            fillcolor = 'rgba('+color_scheme[c]+',0.7)',
            stackgroup = 'energy_consumption',
        )
    )
    c = c +1

fig.update_layout(
    showlegend= True,
    xaxis=dict(
        type='linear',
        range=[1950, 2020],
        )
)

fig.show()
fig.to_image(engine = 'kaleido')
fig.write_image('./topics/065_world_energy_consumption_by_source/data_processed/world_energy_consumption_by_source.svg')
