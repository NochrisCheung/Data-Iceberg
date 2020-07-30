import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
import os
import numpy as np
import visualisation_toolkit.chart_format_config as cfc

pio.kaleido.scope.default_format = 'svg'

glassdoor_grades_df = pd.read_csv('./glassdoor/data_processed/ftse100_glassdoor_grades_cleaned.csv')
glassdoor_grades_df.columns = ['index','company_name','rating','review_count','used_review','used_review_%','common_name','website','industry']
company_rating_distribution = glassdoor_grades_df['company_name'].groupby(pd.cut(glassdoor_grades_df['rating'], np.arange(glassdoor_grades_df['rating'].apply(np.floor).min(),glassdoor_grades_df['rating'].apply(np.ceil).max()+0.5, 0.5))).count()

fig = go.Figure()
cfc.configure_chart(fig)

# Plot the scatter graph with data
fig.add_trace(
    go.Histogram(
        x=glassdoor_grades_df['rating'].values,
        xbins=dict(
            start=2.0,
            end=5,
            size=0.5
        )
    )
)

# Define the marker format
fig.update_traces(
    marker = dict(
        cmax = 5,
        cmin = 2,
        color = np.arange(2,5,0.5),
        colorscale = ['lightskyblue','steelblue', 'navy', 'darkslateblue','indigo'],
        reversescale= False
    )
)

# Configure histogram and axes layout
fig.update_layout(
    bargap=0.2, # gap between bars of adjacent location coordinates
)

fig.to_image(engine = 'kaleido')
fig.write_image('./glassdoor/data_processed/ftse100_glassdoor_rating_hist.svg')
