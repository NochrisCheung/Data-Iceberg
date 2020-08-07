import numpy as np
import pandas as pd
import plotly.graph_objects as go
import visualisation_toolkit.chart_format_config as cfc
data_creation = np.array(
    [[2010, 2],
    [2011, 5],
    [2012, 6.5],
    [2013, 9],
    [2014, 12.5],
    [2015, 15.5],
    [2016, 18],
    [2017, 26],
    [2018, 33],
    [2019, 41],
    [2020, 59],
    [2021, 74],
    [2022, 94],
    [2023, 118],
    [2024, 149],
    [2025, 175]]
    )

data_creation_df = pd.DataFrame(data_creation, columns = ['Year','Volume'])
data_creation_df['Amount of Brains'] = data_creation_df['Volume'].transform(lambda x: x*(10**6)/2.5)
data_creation_df
fig = go.Figure()
cfc.configure_chart(fig)

fig.add_trace(
    go.Scatter(
        x = data_creation_df['Year'],
        y = data_creation_df['Amount of Brains'],
        mode = 'text+lines',
        line = dict(
            shape = 'spline',
            width = 3,
            color = 'indigo',
        ),
        text = [str(x/1000000) + 'm' for x in data_creation_df['Amount of Brains']]
    )
)


fig.update_traces(
    textposition = 'top center',
)

fig.update_layout(
    xaxis= dict(
        dtick = 1
    ),
    yaxis = dict(
        showline = False,
        showgrid = False,
        zeroline = False,
        showticklabels=False,
        range = [-10 * 1000000, 75 * 1000000]
    )
)

fig.update_layout(
    width = 1400,
    height = 700,
)

fig.update_layout(
    margin=dict(
        l=45,
        r=15,
        b=60,
        t=180,
        pad = 0
    )
)

fig.write_image('./topics/009_data_creation_growth_analysis/data_processed/data_evolution.svg')
