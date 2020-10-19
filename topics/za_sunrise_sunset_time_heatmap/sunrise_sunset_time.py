import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly
import visualisation_toolkit.chart_format_config as cfc
from datetime import datetime, timedelta

# sun_df = pd.read_excel('./topics/za_sunrise_sunset_time_heatmap/data_processed/day_length.xlsx',sheet_name = 'Sunrise Sunset')
sun_df = pd.read_excel('./topics/za_sunrise_sunset_time_heatmap/data_processed/day_length_edited.xlsx',sheet_name = 'Sunrise Sunset Adjusted')
# sun_df = pd.read_csv('./topics/za_sunrise_sunset_time_heatmap/data_processed/day_length.xlsx - Sunrise Sunset Adjusted.csv')
sun_df.columns = ['2020','1_rise','1_set','2_rise','2_set','3_rise','3_set','4_rise','4_set','5_rise','5_set','6_rise','6_set',
                    '7_rise','7_set','8_rise','8_set','9_rise','9_set','10_rise','10_set','11_rise','11_set','12_rise','12_set']
sun_df = sun_df.loc[2:]
sun_df = sun_df.set_index(['2020'], drop = True)
sun_df.iloc[:,2:2+2].dropna()
sun_df.values


year_sun = pd.DataFrame()
for i in np.arange(0,12):
    month_sun = sun_df.iloc[:,2*i:2*i+2].dropna()
    month_sun.columns = ['sunrise','sunset']
    # if i == 3:
    #     month_sun('sunrise') = [t.hour*60 + t.minute for t in month_sun['sunrise'].values]
    #
    month_sun['sunrise_values'] = [t.hour*60 + t.minute for t in month_sun['sunrise'].values]
    month_sun['sunset_values'] = [t.hour*60 + t.minute for t in month_sun['sunset'].values]
    # month_sun.index = ['2020-'+str(i+1) + '-' + str(d)[0:-2] for d in month_sun.index]
    month_sun.index = [str(i+1) + ':' + str(d)[0:-2] for d in month_sun.index]
    for c in month_sun.columns[0:2]:
        month_sun[c] = ['2020-01-01 '+ str(t) for t in month_sun[c]]
    year_sun = pd.concat([year_sun, month_sun])
    i = i+1
diff = year_sun['sunset_values']-year_sun['sunrise_values']
diff[150:200]
diff.describe()
# year_sun['sunrise'] = pd.to_datetime(year_sun['sunrise'])
# year_sun['sunset'] = pd.to_datetime(year_sun['sunset'])
fig = cfc.configure_chart()

fig.add_trace(
    go.Bar(
        x = year_sun['sunset'].values,
        y = year_sun['sunset'].index,
        orientation = 'h',
        marker = dict(
            # color = 'rgba('+color_scheme[1]+',1)',
            # colorscale = 'Plasma',
            colorscale = plotly.colors.sequential.Pinkyl[0:5],
            color = year_sun['sunset_values'].values,
            # color = 'rgba(33,33,33,1)',
            line = dict(
                # shape = 'spline',
                width = 0,
                # color = 'rgb('+color_scheme[i]+')',
                color = 'rgba(240,248,255,1)',
            ),
        ),
        width = 1
    )
)

fig.add_trace(
    go.Bar(
        x = year_sun['sunrise'].values,
        y = year_sun['sunrise'].index,
        orientation = 'h',
        marker = dict(
            color = 'rgba(240,248,255,1)',
            line = dict(
                # shape = 'spline',
                width = 0.,
                # color = 'rgb('+color_scheme[i]+')',
                color = 'rgba(240,248,255,1)',
            ),
        ),
        width = 1
    )
)

fig['layout']['yaxis']['autorange'] = "reversed"

fig.update_layout(
    barmode = 'overlay',
    showlegend = False,
    yaxis = dict(
        showgrid = False,
        autorange = 'reversed'
    ),
    xaxis = dict(
        range = ['2020-01-01 00:00:00','2020-01-02 00:00:00']
    )
)

fig.show()
fig.write_image('./topics/za_sunrise_sunset_time_heatmap/data_processed/day_length.svg')

# i = 0
# for i in np.arange(0,12):
#     month_sun = sun_df.iloc[:,2*i:2*i+2].dropna()
#     for c in month_sun.columns:
#         month_sun[c] = ['2020-01-01 '+ str(t) for t in month_sun[c]]
#         pd.to_datetime(month_sun[c])
#     fig.add_trace(
#         go.Bar(
#             x = month_sun.iloc[:,1:2].values,
#             y = [str(i)+ ' '+ str(round(d,0)) for d in month_sun.index],
#             orientation = 'h',
#             marker = dict(
#                 color = 'rgba(33,33,33,1)',
#                 line = dict(
#                     # shape = 'spline',
#                     width = 0.,
#                     # color = 'rgb('+color_scheme[i]+')',
#                     color = 'rgba(240,248,255,1)',
#                 ),
#             ),
#             width = 1
#         )
#     )
#     fig.add_trace(
#         go.Bar(
#             x = month_sun.iloc[:,0:1].values,
#             y = [str(i)+ ' '+ str(round(d,0)) for d in month_sun.index],
#             orientation = 'h',
#             marker = dict(
#                 # color = 'rgba('+color_scheme[1]+',1)',
#                 color = 'rgba(240,248,255,1)',
#                 line = dict(
#                     # shape = 'spline',
#                     width = 0,
#                     # color = 'rgb('+color_scheme[i]+')',
#                     color = 'rgba(240,248,255,1)',
#                 ),
#             ),
#             width = 1
#         )
#     )
#     i = i+1
#
# fig.update_layout(
#     barmode = 'overlay',
#     showlegend = False,
#     yaxis = dict(
#         showgrid = False
#     )
# )
#
# fig.show()
