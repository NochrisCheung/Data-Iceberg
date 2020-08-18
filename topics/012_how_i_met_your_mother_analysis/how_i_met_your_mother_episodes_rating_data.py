from imdb import IMDb
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import visualisation_toolkit.chart_format_config as cfc
ia = IMDb()
ia.get_movie_infoset()
# check series how i met your mother
series = ia.get_movie('0460649')

# pd.DataFrame({'a' : np.arange(1,3), 'b' : ['1','2']})
all_ratings_df = pd.DataFrame(columns = ['Season','Episode','Rating'])
ia.update(series,'episodes')

for s in seasons:
    episodes = series['episodes'][s].keys()
    all_ratings = [series['episodes'][s][e]['rating'] for e in episodes]
    new_season_rating = pd.DataFrame({
        'Season' : [s]* max(episodes),
        'Episode' : np.arange(1, max(episodes)+1),
        'Rating' : all_ratings
    })
    all_ratings_df = all_ratings_df.append(new_season_rating)

all_ratings_df['Rating']
all_ratings_df['Rating'] = all_ratings_df['Rating'].round(1)
all_ratings_df.to_csv('./topics/012_how_i_met_your_mother_analysis/data_processed/how_i_met_your_mother_episodes_rating.csv')

for s in seasons:
    print(all_ratings_df[all_ratings_df['Season'] == s]['Rating'].mean())

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
    '33,33,33'
]

fig = go.Figure()
cfc.configure_chart(fig)
for s in seasons:
    episodes = series['episodes'][s].keys()
    fig.add_trace(
        go.Bar(
            name = str(s),
            x = [str(s)+ '-0'] + [str(s)+'-'+str(e) for e in episodes],
            y = pd.Series([0]).append(all_ratings_df[all_ratings_df['Season'] == s]['Rating'], ignore_index = True),
            marker = dict(
                color = 'rgb('+color_scheme[s-1]+')'
            ),
            width = 1,
        )
    )

fig.update_layout(
    showlegend = False,
    yaxis = dict(
        range = [5, 10],
        showgrid = False
    ),
    xaxis = dict(
        showticklabels=False
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
        r=152,
        b=60,
        t=180,
        pad = 5
    )
)

fig.write_image('./topics/012_how_i_met_your_mother_analysis/data_processed/how_i_met_your_mother_episodes_rating.svg')
