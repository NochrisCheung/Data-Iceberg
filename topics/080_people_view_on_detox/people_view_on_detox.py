import pandas as pd
import plotly.graph_objects as go
import visualisation_toolkit.chart_format_config as cfc
import numpy as np

google_df = pd.read_csv('./topics/080_people_view_on_detox/data_processed/detox_google_search.csv')
google_df_filtered = google_df['Category: All categories'][1:]
google_df_filtered.tail(50)
len(google_df_filtered.index)
fig = cfc.configure_chart()

fig.add_traces(
    go.Scatter(
        x = google_df_filtered.index,
        y = google_df_filtered.values,
        mode = 'lines',
        line = dict(
                shape = 'spline',
                width = 3,
                color = 'steelblue',
                # cmax = 5,
                # cmin = 0,
                # color = [int(v)/100 for v in google_df_filtered.values]*5,
                # colorscale = ['lightskyblue','steelblue', 'navy', 'darkslateblue','indigo'],
        )

    )
)

fig.update_layout(
    yaxis = dict(
        showgrid = False,
        dtick = 20
    )

)
fig.write_image('./topics/080_people_view_on_detox/data_processed/detox_google_search.svg')


google_df = google_df[48:]
google_df.columns = ['Google']

google_df.index = pd.to_datetime(google_df.index)
google_df[50:].tail(50)

fig = cfc.configure_chart()

fig.add_traces(
    go.Scatter(
        x = google_df[17:].index,
        y = google_df[17:]['Google'],
        mode = 'lines',
        line = dict(
                shape = 'spline',
                width = 3,
                color = 'steelblue',
        )

    )
)

fig.update_layout(
    yaxis = dict(
        showgrid = False,
        dtick = 20
    )

)
fig.write_image('./topics/022_google_search_google/data_processed/google_search_google.svg')
