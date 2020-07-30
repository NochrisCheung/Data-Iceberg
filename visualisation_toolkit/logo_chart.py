import plotly.graph_objects as go
import plotly.io as pio
import os
import numpy as np
import visualisation_toolkit.chart_format_config as cfc


fig = go.Figure(
    go.Line(
        x = np.arange(1,40,1),
        y = [3,
            6,
            4,
            8,
            12,
            15,
            10,
            15,
            21,
            26,
            28,
            34,
            30,
            23,
            18,
            23,
            30,
            25,
            22,
            34,
            42,
            50,
            45,
            40,
            33,
            39,
            44,
            42,
            47,
            41,
            36,
            33,
            30,
            24,
            19,
            21,
            16,
            10,
            3],
            line = dict(
                width = 5,
                color = 'navy'
            )

    )
)

fig.show()


fig.update_traces(
    marker = dict(
        cmax = 40,
        cmin = 1,
        color = np.arange(1,40,1),
        colorscale = ['lightskyblue','steelblue', 'navy', 'darkslateblue','indigo'],
        reversescale= True,
        line = dict(
            width = 5
        )
    ),
)

fig.update_layout(
    width = 1000,
    height = 1000,
    plot_bgcolor = 'white',
    paper_bgcolor = 'white',
)

# Definte x-axis and y-axis layout
fig.update_layout(
    xaxis = dict(
        showline = False,
        showgrid = False,
        zeroline = False,
    ),
    yaxis = dict(
        showline = False,
        showgrid = False,
        zeroline = False,
    )
)

pio.kaleido.scope.default_format = 'svg'
fig.to_image(engine = 'kaleido')
fig.write_image('./visualisation_toolkit/logo_top.svg')
