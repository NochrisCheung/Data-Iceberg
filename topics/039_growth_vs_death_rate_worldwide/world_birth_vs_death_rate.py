import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from visualisation_toolkit import chart_format_config as cfc
import numpy as np

birth_death_rate_df = pd.read_csv('./data_source/our_world_in_data/world_birth_death_rate/births-and-deaths-projected-to-2100.csv')
world_rate_df = birth_death_rate_df[birth_death_rate_df['Entity'] == 'World'].reset_index(drop = True)
world_rate_df.columns
world_rate_df = world_rate_df[world_rate_df['Year'] <= 2050]
world_rate_df[30:80 ]
def f(x):
    return x[0] + x[1]

d_rate = world_rate_df[['Estimates, 1950 - 2015: Demographic Indicators - Deaths (thousands) (thousands)','Deaths (thousands)']].fillna(0).apply(f, axis = 1)
b_rate = world_rate_df[['Estimates, 1950 - 2015: Demographic Indicators - Births (thousands) (thousands)','Births (thousands)']].fillna(0).apply(f, axis = 1)

fig = cfc.configure_double_axes_chart()

colorscale = ['lightskyblue','steelblue', 'navy', 'darkslateblue','indigo']
i = 0
for col in world_rate_df.columns[3:]:
    if i < 2:
        line_setting = dict(
            shape = 'spline',
            color = colorscale[i],
            width = 3,
        )
    else:
        line_setting = dict(
            shape = 'spline',
            color = colorscale[i-2],
            width = 3,
            dash = 'dash'
        )

    fig.add_trace(
        go.Scatter(
            name = i,
            x = world_rate_df['Year'],
            y = world_rate_df[col],
            mode = 'lines',
            line = line_setting

        ),
        secondary_y = False
    )
    i = i + 1


fig.add_trace(
    go.Scatter(
        name = 'birth_death_ratio',
        x = world_rate_df['Year'],
        y = world_rate_df['Estimates, 1950 - 2015: Demographic Indicators - Deaths (thousands) (thousands)']/world_rate_df['Estimates, 1950 - 2015: Demographic Indicators - Births (thousands) (thousands)'],
        mode = 'lines',
        line = dict(
            shape = 'spline',
            color = colorscale[4],
            width = 5,
        )
    ),
    secondary_y = True
)

fig.add_trace(
    go.Scatter(
        name = 'birth_death_ratio',
        x = world_rate_df['Year'],
        y = world_rate_df['Deaths (thousands)']/world_rate_df['Births (thousands)'],
        mode = 'lines',
        line = dict(
            shape = 'spline',
            color = colorscale[4],
            width = 5,
            dash = 'dash'
        )
    ),
    secondary_y = True
)

fig.update_layout(
    showlegend= False,
    xaxis=dict(
        showticklabels=True,
        dtick = 10,
        ),
    yaxis1=dict(
        type='linear',
        range=[39.99*pow(10,6), 150.0*pow(10,6)],
        ),
    yaxis2 = dict(
        type = 'linear',
        range = [0, 1.1],
        showline = False,
        showgrid = False,
        zeroline = False,
        showticklabels=True
        )

)

fig.update_layout(
    margin=dict(
        l=70,
        r=10,
        b=60,
        t=180,
        pad = 5
    )
)

fig.write_image('./topics/039_growth_vs_death_rate_worldwide/data_processed/world_growth_vs_death_rate.svg')
