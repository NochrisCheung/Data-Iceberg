from imdb import IMDb
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import visualisation_toolkit.chart_format_config as cfc

ia = IMDb()
ia.get_movie_infoset()
# check series how i met your mother
series = ia.get_movie('0898266')

# pd.DataFrame({'a' : np.arange(1,3), 'b' : ['1','2']})
all_ratings_df = pd.DataFrame(columns = ['Season','Episode','Rating'])
ia.update(series,'episodes')
seasons = series['episodes'].keys()
for s in seasons:
    episodes = series['episodes'][s].keys()
    all_ratings = [series['episodes'][s][e]['rating'] for e in episodes]
    # if s == 1:
    #     print('season 1')
    #     epi = np.arange(0, len(episodes))
    # else:
    #     epi = np.arange(1, len(episodes)+1)
    new_season_rating = pd.DataFrame({
        'Season' : [s]* len(episodes),
        'Episode' : np.arange(1, len(episodes)+1),
        'Rating' : all_ratings
    })
    all_ratings_df = all_ratings_df.append(new_season_rating)

all_ratings_df = all_ratings_df.sort_values(by = ['Season','Episode'])
all_ratings_df.head(50)
all_ratings_df['Rating'] = all_ratings_df['Rating'].round(1)
all_ratings_df.to_csv('./topics/075_big_bang_theory_rating/data_processed/big_bang_theory_ratings.csv')

# all_ratings_df[all_ratings_df['Season'] == 1]['Rating'][-1:]
# last_episode = []
# for s in seasons:
#     last_episode = last_episode + all_ratings_df[all_ratings_df['Season'] == s]['Rating'][-1:].to_list()
# sum(last_episode)/10
all_ratings_df['Rating'].mean()
# all_ratings_df['Rating']
all_ratings_df.groupby(by = 'Season').mean().round(1)

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
    '33,33,33',
    '33,33,33',
    '33,33,33',
    '33,33,33',
    '33,33,33',
    '33,33,33'
]

fig = cfc.configure_chart()
for s in all_ratings_df['Season'].unique():
    episodes = all_ratings_df[all_ratings_df['Season']==s]['Episode'].values
    X = [str(s)+ ':0'] + [str(s)+':'+str(e) for e in episodes],
    Y = pd.Series([0]).append(all_ratings_df[all_ratings_df['Season'] == s]['Rating'], ignore_index = True),
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
