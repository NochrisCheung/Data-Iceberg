import pandas as pd
import plotly.graph_objects as go
import visualisation_toolkit.chart_format_config as cfc

average_viewers_by_games = [
    ['All Other Games Combined',689257],
    ['Just Chatting',224836],
    ['Fall Guys',187045],
    ['League of Legends',182173],
    ['Fortnite',121904	],
    ['Grand Theft Auto V',113360],
    ['Call of Duty: Modern Warfare',111980],
    ['VALORANT',92942],
    ['Minecraft',60020],
    ['Counter-Strike: Global Offensive',55841],
    ['Dota 2',45596],
    ['World of Warcraft',43247],
    ['Hearthstone',36517],
    ['Among Us',36487],
    ['Dead by Daylight',28197],
    ['Apex Legends',27794],
    ['Music & Performing Arts',27184],
    ['Escape From Tarkov',22593],
    ['Overwatch',16870],
    ['Tom Clancys Rainbow Six: Siege',16274]
]

average_viewers_by_games_df = pd.DataFrame(average_viewers_by_games, columns = ['name','viewer'])

average_viewers_by_games_df.to_csv('./topics/019_twitch_analysis/data_processed/20200816_past_7_days_average_viewers_by_games.csv')
average_viewers_by_games_df.loc[0,'viewer'] = average_viewers_by_games_df.loc[0,'viewer'] + average_viewers_by_games_df.loc[10:,'viewer'].sum()
average_viewers_by_games_df = average_viewers_by_games_df[0:10]
average_viewers_by_games_df
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

fig.add_trace(
    go.Sunburst(
        labels = ['total'] + average_viewers_by_games_df['name'][::-1].to_list(),
        parents = ['']+ ['total']*10 ,
        values = [average_viewers_by_games_df['viewer'].sum()] + average_viewers_by_games_df['viewer'][::-1].to_list(),
        branchvalues = 'total',
    )
)

fig.update_traces(
    marker = dict(
        colors = ['rgb(255,255,255)'] + ['rgb('+c+')' for c in color_scheme]
        # size = 10
        # ,'white'],
    ),
    textinfo = 'none'
)

fig.update_layout(
     showlegend = False,
     margin=dict(
         l=30,
         r=30,
         b=60,
         t=180,
         pad = 5
     ),
     polar = dict(
        angularaxis = dict(
            direction ='counterclockwise',
        )
    )
)

fig.write_image('./topics/019_twitch_analysis/data_processed/20200816_past_7_days_average_viewers_by_games.svg')
