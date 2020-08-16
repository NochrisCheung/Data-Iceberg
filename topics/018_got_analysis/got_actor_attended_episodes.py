from imdb import IMDb
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import visualisation_toolkit.chart_format_config as cfc
import re

ia = IMDb()
ia.get_movie_infoset()

# check series game of throne
series = ia.get_movie('0944947')

# ia.update(series,'episodes')
ia.update(series,'episodes')
ia.update(series,'full credits')
all_cast_list = series['cast']
all_cast_ids = [c.getID() for c in all_cast_list]
all_cast_df = pd.DataFrame(columns = ['Season','Episode','Cast','Name'])
seasons = []
for key in series['episodes'].keys():
    temp = [key]
    seasons.append(key)
seasons.sort()

for s in seasons:
    print(s)
    episodes = series['episodes'][s].keys()
    all_episode_id = [series['episodes'][s][e].getID() for e in episodes]
    cast_list = []
    name_list = []

    for e in episodes:
        print(e)
        epi_info = ia.get_movie(all_episode_id[e-1])
        ia.update(epi_info, 'full credits')
        cast_list = cast_list + [[p.getID() for p in epi_info['cast']]]
        name_list = name_list + [[p['name'] for p in epi_info['cast']]]

    new_season_cast = pd.DataFrame({
        'Season' : [s]* max(episodes),
        'Episode' : np.arange(1, max(episodes)+1),
        'Cast' : cast_list,
        'Name' : name_list,
    })
    all_cast_df = all_cast_df.append(new_season_cast)

all_cast_df.to_csv('./topics/018_got_analysis/data_processed/got_crew_list_by_episode.csv')
all_cast_df.reset_index()   
per_episode_cast_ids = all_cast_df['Cast']

id_appearance_count = []
for id in cast_ids:
    id_appearance_count = id_appearance_count + [[id, sum([1 if id in e else 0 for e in per_episode_cast_ids])]]

all_cast_df.to_csv('./topics/018_got_analysis/data_processed/got_crew_list_by_episode.csv')

actor_appearance_df = pd.DataFrame(id_appearance_count, columns = ['id','appearance'])
actor_appearance_df = actor_appearance_df.sort_values('appearance', ascending = False).reset_index(drop = True)

appearance_group = []
for a in actor_appearance_df['appearance']:
    if a>=20:
        appearance_group = appearance_group + ['indigo']
    elif a>=10:
        appearance_group = appearance_group + ['darkslateblue']
    elif a>=5:
        appearance_group = appearance_group + ['navy']
    elif a>=2:
        appearance_group = appearance_group + ['steelblue']
    else:
        appearance_group = appearance_group + ['lightskyblue']

sum([1 if c == 'indigo' else 0 for c in appearance_group])
sum([1 if c == 'darkslateblue' else 0 for c in appearance_group])
sum([1 if c == 'navy' else 0 for c in appearance_group])
sum([1 if c == 'steelblue' else 0 for c in appearance_group])
sum([1 if c == 'lightskyblue' else 0 for c in appearance_group])



fig = cfc.configure_chart()
# list(np.arange(1,834)).div(actor_appearance_df['id'].to_list())
# actor_appearance_df.index

fig.add_trace(
    go.Bar(
        name = str(s),

        y = actor_appearance_df['appearance'],
        marker = dict(
            color = 'darkslateblue',
            line = dict(
                width = 0.1
            )
        ),
        width = 1,
    )
)

fig.update_layout(
    showlegend = False,
    yaxis = dict(
        # range = [0, 100],
        showgrid = False
    ),
    xaxis = dict(
        showticklabels=True
        # tickformat = '%'
    )
)

fig.write_image('./topics/018_got_analysis/data_processed/actors_apperance.svg')


top_actor_appearance_df = actor_appearance_df.head(30)
top_actor_appearance_df['actor name'] = [ia.get_person(id)['name'] for id in top_actor_appearance_df['id']]
top_actor_appearance_df

actor_role_list = []
for a in top_actor_appearance_df['actor name']:
    for c in all_cast_list:
        if c['name'] == a:
            actor_role_list = actor_role_list + [[a, c.currentRole['name']]]
            break

appearance_group = []
for a in top_actor_appearance_df['appearance']:
    if a>=60:
        appearance_group = appearance_group + ['indigo']
    elif a>=40:
        appearance_group = appearance_group + ['darkslateblue']
    else:
        appearance_group = appearance_group + ['navy']

actor_role_list

fig2 = cfc.configure_chart()

fig2.add_trace(
    go.Bar(
        name = str(s),
        x = [a for a, r in actor_role_list],
        y = top_actor_appearance_df['appearance'],
        marker = dict(
            color = appearance_group ,
            line = dict(
                width = 1
            )
        ),
        width = 1,
    )
)

fig2.update_layout(
    showlegend = False,
    yaxis = dict(
        range = [20, 70],
        showgrid = False
    ),
    xaxis = dict(
        showticklabels = True,
        tickangle = 0,
        # tickformat = '%'
    )
)

fig2.update_layout(
    margin=dict(
        l=60,
        r=30,
        b=60,
        t=180,
        pad = 5
    )
)


fig2.write_image('./topics/018_got_analysis/data_processed/top_actors_apperance.svg')
