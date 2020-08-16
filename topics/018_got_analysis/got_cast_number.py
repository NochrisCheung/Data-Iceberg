from imdb import IMDb
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import visualisation_toolkit.chart_format_config as cfc
import re

ia.get_movie_infoset()

# check series game of throne
series = ia.get_movie('0944947')

# ia.update(series,'episodes')
ia.update(series,'episodes')
all_cast_df = pd.DataFrame(columns = ['Season','Episode','Cast Number'])
seasons = []
for key in series['episodes'].keys():
    temp = [key]
    seasons.append(key)
seasons.sort()

for s in seasons:
    print(s)
    episodes = series['episodes'][s].keys()
    all_episode_id = [series['episodes'][s][e].getID() for e in episodes]
    cast_len_list = []

    for e in episodes:
        print(e)
        epi_info = ia.get_movie(all_episode_id[e-1])
        ia.update(epi_info, 'full credits')
        cast_len_list = cast_len_list + [len(epi_info['cast'])]

    new_season_cast = pd.DataFrame({
        'Season' : [s]* max(episodes),
        'Episode' : np.arange(1, max(episodes)+1),
        'Cast Number' : cast_len_list
    })
    all_cast_df = all_cast_df.append(new_season_cast)

all_cast_df.to_csv('./topics/018_got_analysis/data_processed/got_crew_count.csv')

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


fig = cfc.configure_chart()
for s in seasons:
    episodes = series['episodes'][s].keys()
    fig.add_trace(
        go.Bar(
            name = str(s),
            x = [str(s)+ '-0'] + [str(s)+'-'+str(e) for e in episodes],
            y = pd.Series([0]).append(all_cast_df[all_cast_df['Season'] == s]['Cast Number'], ignore_index = True),
            marker = dict(
                color = 'rgb('+color_scheme[s-1]+')'
            ),
            width = 1,
        )
    )

fig.update_layout(
    showlegend = False,
    yaxis = dict(
        range = [0, 100],
        showgrid = False
    ),
    xaxis = dict(
        showticklabels=False
    )
)


series['episodes']
