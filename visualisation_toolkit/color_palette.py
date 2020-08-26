import plotly.graph_objects as go
import numpy as np

fig = go.Figure(
    go.Bar(
        x = [1,2,3,4,5],
        y = [1,2,3,4,5]
    )
)

fig.update_traces(
    marker = dict(
        cmin = 0,
        cmax = 5,
        color = np.arange(0,5,1),
        colorscale = ['lightskyblue','steelblue', 'navy', 'darkslateblue','indigo','white'],
    )
)

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
