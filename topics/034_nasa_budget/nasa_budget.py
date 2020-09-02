from imdb import IMDb
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import visualisation_toolkit.chart_format_config as cfc




nasa_df = pd.read_csv('./topics/034_nasa_budget/data_processed/Nasa Budget - budget.csv')
nasa_df.columns

colorscale = ['lightskyblue','steelblue', 'navy', 'darkslateblue','indigo']
fig = cfc.configure_double_axes_chart()

fig.add_trace(
    go.Scatter(
        name = '2014 Constant Dollars',
        x = nasa_df['Year'],
        y = nasa_df['2014 Constant Dollars\n(Millions)']*1000,
        mode = 'lines',
        line = dict(
            shape = 'spline',
            color = colorscale[0],
            width = 3,
        )
    ),
    secondary_y = False
)

fig.add_trace(
    go.Scatter(
        name = '% of Fed Budget',
        x = nasa_df['Year'],
        y = [float(n[:-1])/100 for n in nasa_df['% of Fed Budget']],
        mode = 'lines',
        line = dict(
            shape = 'spline',
            color = colorscale[4],
            width = 3,
        )
    ),
    secondary_y = True
)

fig.update_layout(
    showlegend= False,
    xaxis=dict(
        showticklabels=True
        ),
    yaxis1=dict(
        type='linear',
        dtick  = 10000000
        # range=[289.8*10**9, 355*10**9],
        ),
    yaxis2 = dict(
        type = 'linear',
        tickformat = '.1%',
        range = [-0.0017, 0.046],
        dtick = 0.01,
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

fig.write_image('./topics/034_nasa_budget/data_processed/nasa_budget.svg')
