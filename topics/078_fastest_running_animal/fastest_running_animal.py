import pandas as pd
import plotly.graph_objects as go
import visualisation_toolkit.chart_format_config as cfc

speed_df = pd.read_csv('./topics/078_fastest_running_animal/data_processed/fastest_running_mammals - Speed.csv')

speed_df_filtered = speed_df[['Animal','Quantified Speed km']].sort_values('Quantified Speed km')
speed_df_filtered

fig = cfc.configure_chart()

fig.add_trace(
    go.Bar(
        x = speed_df_filtered['Quantified Speed km'],
        y = speed_df_filtered['Animal'],
        orientation = 'h',
        width = 0.5,

        text = [round(s) for s in speed_df_filtered['Quantified Speed km']],
        textposition = 'outside',
        textfont = dict( size = 16)
    )
)

fig.update_layout(
    xaxis = dict(
        showticklabels = False,
        range = [0,150]
    ),
    yaxis = dict(
        showgrid = False,
        showticklabels = True
    )
)

fig.write_image('./topics/078_fastest_running_animal/data_processed/fastest_running_mammals.svg')
