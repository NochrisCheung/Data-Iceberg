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
