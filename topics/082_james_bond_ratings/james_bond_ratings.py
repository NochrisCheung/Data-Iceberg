from imdb import IMDb
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import visualisation_toolkit.chart_format_config as cfc

ia = IMDb()
ia.get_movie_infoset()
movies = ia.get_keyword('007')

filtered_movie = []
for m in movies:
    if 'Commercial' not in m['title'] and 'Radio' not in m['title'] and 'Official' not in m['title'] and 'Madonna' not in m['title'] and 'Heineken\'s' not in m['title'] and 'No Time to Die' not in m['title']:
        filtered_movie = filtered_movie + [m]

mov_name = []
mov_actor = []
mov_rating = []
mov_year = []

for fm in filtered_movie:
    ind_mov = ia.get_movie(fm.movieID)
    mov_name = mov_name + [ind_mov['title']]
    mov_actor = mov_actor + [ind_mov['cast'][0]['name']]
    mov_rating = mov_rating + [ind_mov['rating']]
    mov_year = mov_year + [ind_mov['year']]

series = pd.DataFrame(list(zip(mov_name,mov_actor,mov_rating,mov_year)),columns = ['name','actor','rating','year'])
series = series[:26]
series = series.sort_values('year')
actor_list = series['actor'].unique().tolist()
series

len(filtered_movie)
series.to_csv('./topics/082_james_bond_ratings/data_processed/james_bond_ratings.csv')

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
    '33,33,33',
]

fig = cfc.configure_chart()
fig.add_trace(
    go.Bar(
        name = str(s),
        x = X[0],
        y = Y[0],
        marker = dict(
            color = 'rgb('+color_scheme[s-1]+')'
        ),
        width = 1,
    )
)

episodes = series['episodes'][10].keys()
X = ['10:0'] + ['10:'+str(e) for e in episodes],
Y = pd.Series([0]).append(all_ratings_df[all_ratings_df['Season'] == 10]['Rating'], ignore_index = True),
fig.add_trace(
    go.Bar(
        name = '10',
        x = X[0],
        y = Y[0],
        marker = dict(
            color = 'rgb('+color_scheme[10-1]+')'
        ),
        width = 1,
    )
)


fig.show()
fig.update_layout(
    showlegend = False,
    yaxis = dict(
        range = [5, 10],
        showgrid = False
    ),
    xaxis = dict(
        showticklabels=True
    )
)

fig.update_layout(
    width = 1400,
    barmode = 'group',
    bargap = 0,
    bargroupgap = 0,
)

fig.update_layout(
    margin=dict(
        l=52,
        r=25,
        b=60,
        t=180,
        pad = 5
    )
)

fig.write_image('./topics/075_big_bang_theory_rating/data_processed/big_bang_theory_ratings.svg')
