import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import visualisation_toolkit.chart_format_config as cfc



partner_df = pd.read_csv('./topics/077_number_of_partners_before_marriage/data_processed/number_of_partner_before_marriage_by_marriage_cohort - record.csv')
partner_df['Partners'] = partner_df['Partners'].astype('string')

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
i = 0
for col in partner_df.columns[1:]:
    fig.add_trace(
        go.Scatter(
            name = col,
            x = [str(p) + ' partners' for p in partner_df['Partners']],
            y = partner_df[col].values,
            mode = 'markers+lines',
            line = dict(
                width = 8,
                color = 'rgb('+color_scheme[i]+')'
            ),
            marker = dict(
                size = 8,
                # [30 if i == 10 else 10],
                color = 'rgb('+color_scheme[i]+')'
            )
        ),
    )
    i = i + 1

fig.show()
fig.update_layout(
    yaxis = dict(
        tickformat = ',.0%',
        dtick = 0.1
    )
)

fig.update_layout(
    margin=dict(
        l=60,
        r=30,
        b=60,
        t=180,
        pad = 5
    )
)

fig.to_image(engine = 'kaleido')
fig.write_image('topics/077_number_of_partners_before_marriage/data_processed/number_of_partner_before_marriage_by_marriage_cohort.svg')
