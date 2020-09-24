import pandas as pd
import plotly.graph_objects as go
import visualisation_toolkit.chart_format_config as cfc

pornhub_df = pd.read_excel('./topics/048_pornhub_user/data_processed/video.xlsx')
time_df = pornhub_df.iloc[0:20,0:4]
time_df = time_df.sort_values(by = 'Total Min', ascending = True)
time_df
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
    go.Bar(
        x = time_df['Total Min'],
        y = time_df['Top 20 traffic'],
        orientation = 'h',
        # marker = dict(
            # color = [condiment_df['Condiment'].ne(c).idxmin() for c in condiment_df['Condiment'].iloc[::-1]],
            # color = ['rgb('+c+')' for c in color_scheme[0:8]],
            # colorscale = ['lightskyblue','steelblue', 'navy'],
            # opacity = 0.9,
            # line = dict(
                # color = [condiment_df['Condiment'].ne(c).idxmin() for c in condiment_df['Condiment'].iloc[::-1]],
                # color = ['rgb('+c+')' for c in color_scheme[0:8]]
                # colorscale = ['lightskyblue','steelblue', 'navy'],
            # )
        # ),
        width = 0.5,
        text = [str(h)[:-2]+' min '+str(m)[:-2]+ ' sec' for h, m in zip(time_df['Hr'],time_df['Min'])],
        textposition = 'outside',
        textfont = dict( size = 16)
    )
)

fig.update_layout(
    xaxis = dict(
        showticklabels = False,
        range = [500,700]
    ),
    yaxis = dict(
        showgrid = False,
        showticklabels = True
    )
)
    #
    # fig.update_layout(
    #     margin=dict(
    #         l=90,
    #         r=90,
    #         b=40,
    #         t=200,
    #         pad = 5
    #     )
    # )
fig.write_image('./topics/048_pornhub_user/data_processed/pornhub_time.svg')
