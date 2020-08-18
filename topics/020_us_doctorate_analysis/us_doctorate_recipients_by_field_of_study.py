import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import visualisation_toolkit.chart_format_config as cfc

phd_df = pd.read_csv('./data_source/ncses/doctorrate/us_doctorate_type.xlsx - Doctorate recipients, by major field of study_ Selected years, 1988–2018.csv')

phd_df
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
    go.Scatter(
        x = phd_df.columns[1:].astype(str),
        y = phd_df.loc[0][1:],
        mode = 'markers+lines',
        marker = dict(
            color = 'rgb(33,33,33)'
        ),
        line = dict(
            shape = 'spline',
            width = 3,
            color = 'rgb(33,33,33)',
        ),
    ),
    # row = 2, col = 1

)


for i in range(1,9):
    fig.add_trace(
        go.Bar(
            x = phd_df.columns[1:].astype(str),
            y = phd_df.loc[i][1:],
            # mode = 'lines',
            marker = dict(
                color = 'rgbA('+color_scheme[i]+',1)',
                line = dict(
                    # shape = 'spline',
                    width = 1,
                    # color = 'rgb('+color_scheme[i]+')',
                    color = 'rgb(33,33,33)',
                ),
            )
            # line = dict(
            #     shape = 'spline',
            #     width = 3,
            #     color = 'rgb('+color_scheme[i]+')',
            # ),
            # fillcolor = 'rgba('+color_scheme[i]+',0.8)',
            # stackgroup = 'field',
            # barmode = 'stack'
            )
    )

fig.update_layout(
    barmode = 'stack'
)

fig.update_layout(
    showlegend = False,
    xaxis = dict(
        # range = [1988, 2018],
        # dtick = 5
         # tickmode = 'array',
         # tickvals = [0,1,2,3,4,5,6,7],
         # ticktext = ['1988', '1993','1998','2003','2008','2013','2018']
         tick0 = 1988,
         dtick = 5
    ),
    yaxis = dict(
        showgrid = False
    )
)



fig.write_image('./topics/020_us_doctorate_analysis/data_processed/us_doctorate_recipients_by_field_of_study.svg')
