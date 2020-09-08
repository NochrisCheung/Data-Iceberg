import pandas as pd
import plotly.graph_objects as go
import visualisation_toolkit.chart_format_config as cfc

street_df = pd.read_csv('./topics/037_uk_most_frequent_street_name/data_processed/UK Most Frequent Street Name - Name.csv')street_df = condiment_df.sort_values(by = 'Sales (£m)', ascending = True)
street_df = street_df.sort_values(by = 'Frequency', ascending = True)
street_df
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
        x = street_df['Frequency'],
        y = street_df['Street Name'],
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
        width = 0.5
    )
)

fig.update_layout(
    xaxis = dict(
        showticklabels = False
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
fig.write_image('./topics/037_uk_most_frequent_street_name/data_processed/uk_most_frequent_road_name.svg')
