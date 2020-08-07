import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
import os
import uk_employment_sponsor.code.chart_format_config

# from .chart_format_config import *

pio.kaleido.scope.default_format = 'svg'

cwd = os.path.dirname(os.path.realpath('__file__'))

sponsor_df = pd.read_csv(cwd + '/uk_employment_sponsor/data_source/UKTiersponsors_All.csv')
sponsor_by_tier_type_by_industry = sponsor_df.pivot_table(values = 'Town', index= 'Industry', columns = 'Main Tier', aggfunc = 'count')
tier_2_columns = [col for col in sponsor_by_tier_type_by_industry.columns if 'Tier 2' in col]
sponsor_by_industry = sponsor_by_tier_type_by_industry[tier_2_columns].sum(axis = 1)
sponsor_by_industry.sort_values(ascending = False).head(10)

fig = go.Figure()

fig.add_trace(
        go.Pie(
            # name = 'Q'+str(i),
            labels = sponsor_by_industry.index,
            values = sponsor_by_industry.values,
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
