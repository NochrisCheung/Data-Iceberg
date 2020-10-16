import pandas as pd
import plotly.graph_objects as go
import visualisation_toolkit.chart_format_config as cfc

ratings = pd.read_csv('topics/055_harry_potter_movie_and_book/data_processed/harry_potter_book_and_movie_ratings - ratings.csv')

ratings

fig = cfc.configure_double_axes_chart()

fig.add_trace(
    go.Scatter(
        mode = 'markers',
        x = ratings['Book'][0:7].index.tolist(),
        y = ratings['Book'][0:7].tolist(),
        marker = dict(
            size = 20,
            line = dict(
                width = 0
            ),
            symbol = 'star'
        )
    ),
    secondary_y = True
)

fig.add_trace(
    go.Bar(
        x = ratings['Movie'][0:7].index.tolist(),
        y = ratings['Movie'][0:7].tolist(),
        width = 0.4
    ),
    secondary_y = False
)

fig.add_trace(
    go.Bar(
        x = ratings['Movie'][0:7].index.tolist(),
        y = ratings['Movie'][0:6].tolist()+[ratings['Movie'][7].tolist()],
        width = 0.4
    ),
    secondary_y = False
)

fig.update_layout(
    showlegend= False,
    xaxis=dict(
        # showticklabels=True,
        # dtick = 10,
        ),
    yaxis2=dict(
        range=[0,5],
        showgrid = False,
        ),
    yaxis1 = dict(
        type = 'linear',
        range = [0, 10],
        showline = False,
        showgrid = False,
        zeroline = False,
        showticklabels=True
        ),
        margin=dict(
            l=60,
            r=30,
            b=60,
            t=190,
            pad = 5
        )
)

fig.write_image('topics/055_harry_potter_movie_and_book/data_processed/harry_potter_book_and_movie_ratings.svg')
