import pandas as pd
import plotly.graph_objects as go
import visualisation_toolkit.chart_format_config as cfc


google_df = pd.read_csv('./data_source/google_trend/google_trend_search_google/multiTimeline.csv')

google_df = google_df[1:]
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
