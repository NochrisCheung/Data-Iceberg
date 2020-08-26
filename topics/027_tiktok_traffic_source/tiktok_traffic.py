import pandas as pd
import plotly.graph_objects as go
import visualisation_toolkit.chart_format_config as cfc
import numpy as np

traffic_source = [
                ['Source', '%'],
                ['Direct', 0.061],
                ['Search', 0.562],
                ['Mail', 0.004],
                ['Referrals', 0.342],
                ['Social', 0.028],
                ['Display Ads', 0.000],
                ['Total', 1]
                ]

source_df = pd.DataFrame(traffic_source[1:], columns = traffic_source[0])

source_df.to_csv('./topics/027_tiktok_traffic_source/data_processed/tiktok_traffic.csv')

tiktik_color_scheme = [
    '47,67,97',
    '238,29,82',
    '33,33,33',
    '105,201,208',
    '75,0,130',
    '1,1,1'
]
fig = cfc.configure_chart()

fig.add_traces(
    go.Sankey(
        node = dict(
            pad = 15,
            thickness = 20,
            line = dict(
                width = 0
            ),
            color = ['rgb('+tiktik_color_scheme[i]+')' for i in np.arange(0,6)],
            label = source_df['Source'].tolist()
        ),
        link = dict(
            source = [0, 1, 2, 3, 4, 5],
            target = [6, 6, 6, 6, 6, 6],
            value = source_df['%'].tolist(),
            color = ['rgba('+tiktik_color_scheme[i]+',0.5)' for i in np.arange(0,6)]
        )
    )
)




fig.write_image('topics/027_tiktok_traffic_source/data_processed/tiktok_traffic.svg')
