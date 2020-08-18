import pandas as pd
import numpy as np
import plotly.graph_objects as go
import visualisation_toolkit.chart_format_config as cfc


nobel_lau_df = pd.read_excel('./data_source/wikipedia/nobel_prize_laureates/nobel_prize_laureates.xlsx',header = None)
nobel_lau_df['laureates'] = [nobel_lau_df[0][i]
                            if any([1 if char.isdigit() else 0 for char in nobel_lau_df[0][i]])
                            else ''
                            for i in np.arange(0, len(nobel_lau_df))]


country_list = []
for item in nobel_lau_df[0]:
    if any([1 if char.isdigit() else 0 for char in item ]) == False:
        country = item
    country_list = country_list + [country]

country_df = pd.DataFrame(country_list, columns = ['nationality'])
new_nobel_lau_df = pd.concat([country_df, nobel_lau_df], axis = 1)
new_nobel_lau_df = new_nobel_lau_df[new_nobel_lau_df['laureates'] != ''][['laureates','nationality']].reset_index(drop = True)

year_list = []
for item in new_nobel_lau_df['laureates']:
    [item_year] = [''.join([char if char.isdigit() else '' for char in str(item)])]
    if len(item_year) > 4:
        item_year = item_year[-4:]
    year_list = year_list + [item_year]

new_nobel_lau_df['year awarded'] = year_list

new_nobel_lau_df = new_nobel_lau_df[new_nobel_lau_df['year awarded'] != '']
new_nobel_lau_df['year awarded'] = new_nobel_lau_df['year awarded'].astype(int)
nobel_lau_after_1990_df = new_nobel_lau_df[new_nobel_lau_df['year awarded'] >= 2000].reset_index(drop = True)

remove_keyword_list = ['born', '(now', 'now', 'citizenship', 'based', 'moved', 'under', 'as', ' egypt', 'egypt', 'jr.']
prize_type = []
for lau in nobel_lau_after_1990_df['laureates']:
    info_list = []
    if len(str(lau).split(',')) > 3:
        for info_chunk in str(lau).split(','):
            if any([1 if (i if i == '' else i[0].lower() + i[1:]) in remove_keyword_list else 0 for i in info_chunk.split(' ')]):
                continue
            else:
                info_list = info_list + [info_chunk]
    else:
        info_list = str(lau).split(',')

    prize_type = prize_type + [info_list[1][1:] if info_list[1][0] == ' ' else info_list[1]]


prize_type_df = pd.DataFrame(prize_type, columns = ['prize category'])

nobel_prize_after_1990_all_info = pd.concat([nobel_lau_after_1990_df, prize_type_df], axis = 1)

nobel_prize_after_1990_all_info.columns


nobel_prize_after_1990_all_info['prize category'].unique()

fig = cfc.configure_chart()
fig.add_traces(
    go.Scatter(
        y = nobel_prize_after_1990_all_info['prize category'],
        x = nobel_prize_after_1990_all_info['year awarded'],
        mode = 'markers',
        marker = dict(
            size = 25,
            color = 'lightsteelblue',
            line = dict(
              width = 2,
              color = 'darkslateblue'
            ),
        ),
        text = nobel_prize_after_1990_all_info['nationality']
    )
)

fig.update_layout(
    showlegend = False,
    # xaxist = dict(
    #     range = [1990, 2019]
    # ),
    yaxis = dict(
        showticklabels = False,
        showgrid = True
    )
)

fig.update_layout(
    margin=dict(
        l=60,
        r=30,
        b=60,
        t=200,
        pad = 5
    )
)

fig.write_image('./topics/zb_nobel_prize_laureates/data_processed/nobel_prize_laureates_by_nationality.svg')
