import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
import os
import uk_employment_sponsor.code.chart_format_config

# from .chart_format_config import *

pio.kaleido.scope.default_format = 'svg'

cwd = os.path.dirname(os.path.realpath('__file__'))

sponsor_df = pd.read_csv(cwd + '/uk_employment_sponsor/data_source/UKTiersponsors_All.csv')

sponsor_df['Date Added'] = pd.to_datetime(sponsor_df['Date Added'])
sponsor_by_tier_type_by_month = sponsor_df.pivot_table(values = 'Town', index= 'Date Added', columns = 'Main Tier', aggfunc = 'count').groupby(pd.Grouper(freq = 'q', closed = 'left',label = 'left')).sum()

tier_2_columns = [col for col in sponsor_by_tier_type_by_month.columns if 'Tier 2' in col]
tier_2_sponsor_by_quarter = sponsor_by_tier_type_by_month[tier_2_columns].sum(axis = 1)

fig = go.Figure()

# for i in range(2014, 2021):
#     fig.add_trace(
#         go.Bar(
#             name = i,
#             x = ['Q1','Q2','Q3','Q4'],
#             y = [val for ind, val in zip(tier_2_sponsor_by_quarter.index, tier_2_sponsor_by_quarter.values) if ind.year == i]
#         )
#     )
# i=1
#
# for i in range(1,5):
#     fig.add_trace(
#         go.Bar(
#             name = 'Q'+str(i),
#             x = tier_2_sponsor_by_quarter.index[1+i::4],
#             y = tier_2_sponsor_by_quarter.values[1+i::4]
#
#         )
#     )

fig.add_trace(
    go.Bar(
        # name = 'Q'+str(i),
        x = tier_2_sponsor_by_quarter.index[1:],
        y = tier_2_sponsor_by_quarter.values[1:],
    )
)

# Configure font
fig.update_layout(
    font = dict(
        size = 16,
        family = 'Oswald'
        )
)

fig.update_traces(
    marker = dict(
        color= tier_2_sponsor_by_quarter.index[1:].values,
        # colorscale = 'Plasma'
        colorscale = ['lightskyblue','steelblue', 'navy', 'darkslateblue','indigo'],
        reversescale= False
    )
    # textposition='middle left'
)
chart_format_config.configure_chart(fig)

# fig.to_image(engine = 'kaleido')
# fig.write_image(cwd + '/../data_processed/year_by_quarter_vs_num_of_new_t2_sponsors.svg')
