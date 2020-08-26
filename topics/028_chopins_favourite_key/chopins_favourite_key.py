import pandas as pd
import plotly.graph_objects as go
import visualisation_toolkit.chart_format_config as cfc

chopin_key = pd.read_csv('./topics/028_chopins_favourite_key/data_processed/Chopin favourite Key - Chopin.csv')

fig = cfc.configure_chart()

fig.add_traces(
    go.Bar(
        x  = chopin_key['Key'],
        y  = chopin_key['Count']
    )
)

fig.write_image('./topics/028_chopins_favourite_key/data_processed/chopins_favourite_key.svg')
