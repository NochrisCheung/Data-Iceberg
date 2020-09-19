import pandas as pd
import plotly.graph_objects as go
import visualisation_toolkit.chart_format_config as cfc

juice_df = pd.read_csv('./topics/047_juice_market_share/data_processed/juice_share_by_litre.csv')
juice_df['int share'] = juice_df['share'].apply(lambda x: int(x[:-1])/100)
juice_df
['total'] + juice_df['flavour'].to_list()
juice_df['int share'].to_list()

fig = cfc.configure_chart()
fig.add_trace(
    go.Pie(
        labels = juice_df['flavour'].to_list(),
        values = juice_df['int share'].to_list(),
        # branchvalues = 'total',
    )
)

fig.update_traces(
    marker = dict(
        colors = ['rgb(255,255,255)'] + ['rgb('+c+')' for c in color_scheme]
        # size = 10
        # ,'white'],
    ),
    textinfo = 'none'
)

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

fig.write_image('./topics/047_juice_market_share/data_processed/fruit_juice_share_by_litre.svg')
