import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import visualisation_toolkit.chart_format_config as cfc

monopoly_df = pd.read_csv('./data_source/truman_collins/monopoly/monopoly_analysis - landing_probability.csv')
monopoly_df = monopoly_df[::-1]
monopoly_df
fig = cfc.configure_chart()

fig.add_trace(
    go.Bar(
        x = monopoly_df['Probability % (Jail Short)'],
        y = monopoly_df['Square'].index,
        marker = dict(
            # color = [color_dict[c] for c in roi_calculation['color']]
            color = monopoly_df['Probability % (Jail Short)'],
            colorscale = ['red','yellow','green'],
            # reversescale = True
            line = dict(
                width = 0
            ),
        ),
        text = monopoly_df['Square'],
        textposition = 'outside',
        orientation = 'h',
    )
)

fig.write_image('./topics/017_monopoly_analysis/data_processed/square_probablity.svg')
