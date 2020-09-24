import pandas as pd
import numpy as np
import plotly.graph_objects as go
import visualisation_toolkit.chart_format_config as cfc

country_uni_count = pd.read_csv('./topics/044_university_ranking_worldwide/data_processed/Uni_Ranking_Top_100.xlsx - Top 100 Data.csv')
uni_count_11_and_21 = country_uni_count[country_uni_count['Year'].isin([2011,2021])]
country_2011 = country_uni_count[country_uni_count['Year'] == 2011]['Country'].unique().tolist()
country_2021 = country_uni_count[country_uni_count['Year'] == 2021].sort_values('Count', ascending = True)['Country'].unique().tolist()
country_list = list(set.intersection(set(country_2021),set(country_2011)))

uni_count_11_and_21 = uni_count_11_and_21.sort_values('Count', ascending = True)
uni_count_11_and_21['Country'].unique()
uni_count_11_and_21.sort_values(by = ['Country', 'Year'])
fig = cfc.configure_chart()
# uni_count_11_and_21[uni_count_11_and_21['Country'].isin(country_list)]['Country'].unique()
for c in uni_count_11_and_21['Country'].unique():
    # ind = list(uni_count_11_and_21[uni_count_11_and_21['Country'].isin(country_list)]['Country'].unique()).index(c)
    ind = uni_count_11_and_21['Country'].unique().tolist().index(c)
    fig.add_trace(
        go.Scatter(
            name = c,
            x = uni_count_11_and_21[uni_count_11_and_21['Country'] == c].sort_values('Year')['Count'],
            y = [ind, ind],
            marker = dict(
                size = 15,
                color = ['lightskyblue','indigo'],
            ),
            line = dict(
                color = 'lightsteelblue',
                width = 3
            )
        )
    )

fig.update_layout(
    showlegend = False,
    xaxis = dict(
        # zeroline = False,
        # showticklabels = True,
        # showgrid = True,
        gridcolor = 'lightsteelblue',
        # range = [25,31.1],
        # dtick = 1
    ),
    yaxis = dict(
        zeroline = False,
        showgrid = False,
        showticklabels = True,
        dtick  = 1
    )
)

fig.show()

fig.write_image('./topics/044_university_ranking_worldwide/data_processed/country_top_uni.svg')
