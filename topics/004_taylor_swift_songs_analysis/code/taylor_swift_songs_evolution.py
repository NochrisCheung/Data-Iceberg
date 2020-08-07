import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import visualisation_toolkit.chart_format_config as cfc

ts_df = pd.read_csv('./google_trend/data_processed/taylor_swift_songs_evolution.csv')

fig = go.Figure()
fig = make_subplots(rows=2, cols=2, row_heights=[0.9, 0.1], column_widths=[0.7, 0.3], horizontal_spacing = 0.01, vertical_spacing= 0.04)
cfc.configure_chart(fig)

song_list = ts_df.columns[1:]
song_color_dict = {
    'Love Story' : '65,105,225',
    'We Are Never Ever Getting Back Together' : '127,255,212',
    'I Knew You Were Trouble' : '144,238,144',
    '22' : '240,230,140',
    'Shake It Off' : '255,160,122',
    'Blank Space' : '205,92,92',
    'Bad Blood' : '219,112,147',
    'I Don’t Wanna Live Forever' : '186,85,211',
    'Look What You Made Me Do' : '147,112,219',
}

# Plot song evolution curves
for song in song_list:
    fig.add_trace(
        go.Scatter(
            name = song,
            x = ts_df['Period'][1:],
            y = ts_df[song][1:],
            mode='lines',
            line = dict(
                shape = 'spline',
                width = 3,
                color = 'rgb('+song_color_dict[song]+')',
            )
        ),
        row = 1,
        col = 1
    )

# Plot peak values
max_values = ts_df.max()[1:].to_list()
max_values
cum_occ = [1, 1, 1, 1, 2, 1, 1, 1, 2]

fill_color_list = ['rgba('+song_color_dict[song]+',0)' for song in song_list]
line_color_list = ['rgb('+song_color_dict[song]+')' for song in song_list]
fig.add_trace(
    go.Scatter(
        name = 'Peak Values',
        x = cum_occ,
        y = max_values,
        mode='markers',
        marker = dict(
            color = fill_color_list,
            size = 10,
            symbol = 'line-ew',
            line_width = 3,
            line_color = line_color_list
        )
    ),
    row = 1,
    col = 2,
)

# Plot half life

half_life_period = [13, 4, 5, 6, 9, 6, 3, 4, 3]
cum_occ = [1, 1, 1, 1, 1, 2, 1, 2, 2]

fig.add_trace(
    go.Scatter(
        name = 'Halflife',
        x = half_life_period,
        y = cum_occ,
        mode='markers',
        marker = dict(
            color = fill_color_list,
            size = 10,
            symbol = 'line-ns',
            line_width = 3,
            line_color = line_color_list
        )
    ),
    row = 2,
    col = 1,
)


fig.update_layout(
    showlegend= False,
    xaxis1=dict(
        type='linear',
        range=[0, 24],
        dtick = 4
        ),
    yaxis1=dict(
        type='linear',
        range=[-0.5, 105],
        ),
    xaxis2=dict(
        type='linear',
        range=[0, 10],
        showline = False,
        showgrid = False,
        zeroline = False,
        showticklabels=False
        ),
    yaxis2 = dict(
        type = 'linear',
        range = [-0.5, 105],

        showline = False,
        showgrid = False,
        zeroline = False,
        showticklabels=False,

        ),
    xaxis3 = dict(
        type = 'linear',
        range = [0, 24],
        showline = False,
        showgrid = False,
        zeroline = False,
        showticklabels = False
        ),
    yaxis3 = dict(
        type = 'linear',
        range = [0.5, 3],

        showline = False,
        showgrid = False,
        zeroline = False,
        showticklabels = False
        )
)

fig.update_layout(
    margin=dict(
        l=60,
        r=40,
        b=40,
        t=180,
        pad = 5
    )
)

fig.show()


fig.to_image(engine = 'kaleido')
fig.write_image('./google_trend/data_processed/taylor_swift_songs_evolution.svg')
