import pandas as pd
import plotly.graph_objects as go
import visualisation_toolkit.chart_format_config as cfc

turnoff_df = pd.read_csv('./topics/061_dating_app_stats/data_processed/dating_app_stats - Profile picture turn off.csv')
turnoff_df.columns

fig = cfc.configure_chart()
fig.add_trace(
    go.Pie(
        labels = turnoff_df['Turn off reason'].to_list(),
        values = turnoff_df['Count'].to_list(),
        # branchvalues = 'total',
    )
)

# fig.update_traces(
#     marker = dict(
#         colors = ['rgb(255,255,255)'] + ['rgb('+c+')' for c in color_scheme]
#         # size = 10
#         # ,'white'],
#     ),
#     textinfo = 'none'
# )

fig.update_layout(
     showlegend = False,
     margin=dict(
         l=30,
         r=30,
         b=60,
         t=180,
         pad = 5
     ),
     polar = dict(
        angularaxis = dict(
            direction ='counterclockwise',
        )
    )
)

fig.write_image('./topics/061_dating_app_stats/data_processed/dating_app_stats - Profile picture turn off.svg')
