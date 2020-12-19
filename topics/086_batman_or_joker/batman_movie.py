from imdb import IMDb
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import visualisation_toolkit.chart_format_config as cfc

ia = IMDb()
ia.get_movie_infoset()
ia.search_movie('batman')
movies = ia.get_keyword('batman')
movies
filtered_movie = []
for m in movies:
    if '–)' not in m['title']:
        filtered_movie = filtered_movie + [m]
filtered_movie

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
actor_list.reverse()
actor_list

fig = cfc.configure_chart()
for act in actor_list:
    fig.add_trace(
        go.Scatter(
            name = act,
            x = series[series['actor'] == act]['rating'],
            y = series[series['actor'] == act]['actor'],
            mode = 'markers+lines',
            # y = [ n +' - '+ str(y) for n, y in zip(series['name'],series['year'])],
            marker = dict(
                line = dict(
                    width = 1,
                    color = ['rgb('+color_scheme[-1]+')' for a in series[series['actor'] == act]['actor']]
                ),
                color = ['rgb('+color_scheme[actor_list.index(a)]+')' for a in series[series['actor'] == act]['actor']],
                size = 10
            ),
            line = dict(
                color = 'rgb('+color_scheme[actor_list.index(act)]+')'
            ),
            # width = 1,
            orientation = 'h',
        )
    )


fig.add_trace(
    go.Scatter(
        name = 'Average',
        x = series.groupby('actor').mean()['rating'].values,
        y = series.groupby('actor').mean()['rating'].index,
        mode = 'markers',
        marker = dict(
            line = dict(
                width = 1,
                color = ['rgb('+color_scheme[-1]+')' for a in series[series['actor'] == act]['actor']]
            ),
            color = ['rgb('+color_scheme[-1]+')' for a in series[series['actor'] == act]['actor']],
            size = 10
        ),
        orientation = 'h',
    )
)

fig.show()

# fig.add_trace(
#     go.Bar(
#         x = [ n +' - '+ str(y) for n, y in zip(series['name'],series['year'])],
#         y = series['rating'],
#         marker = dict(
#             color = ['rgb('+color_scheme[actor_list.index(a)]+')' for a in series['actor']]
#         ),
#         width = 1,
#     )
# )

fig.update_layout(
    showlegend = False,
    xaxis = dict(
        range = [5, 9],
        showgrid = False
    ),
    yaxis = dict(
        showticklabels=True,
        showgrid = False
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

fig.write_image('./topics/082_james_bond_ratings/data_processed/james_bond_ratings.svg')


fig2 = cfc.configure_chart()
fig2.add_trace(
    go.Bar(
        x = [ n +' - '+ str(y) for n, y in zip(series['name'],series['year'])],
        y = series['rating'],
        marker = dict(
            color = ['rgb('+color_scheme[actor_list.index(a)]+')' for a in series['actor']]
        ),
        width = 1,
    )
)

fig2.update_layout(
    yaxis = dict(
        range = [4,8],
        showgrid = False
    )
)

fig2.update_layout(
    margin=dict(
        l=52,
        r=25,
        b=60,
        t=180,
        pad = 5
    )
)

fig2.write_image('./topics/082_james_bond_ratings/data_processed/james_bond_ratings_by_moveis.svg')
