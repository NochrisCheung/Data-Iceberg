import pandas as pd
import plotly.graph_objects as go
import visualisation_toolkit.chart_format_config as cfc

pasta_cooking = pd.read_excel('./topics/059_pasta_cooking_time/data_processed/pasta.xlsx')
pasta_cooking

fig = cfc.configure_chart()

fig.add_traces(
    go.Bar(
        x = pasta_cooking['Cooking time (min)'].tolist(),
        y = pasta_cooking['Pasta'],
        orientation = 'h',
        width = 0.5
        # marker = dict(
        #     size = 10
        # )
    )
)

fig.add_traces(
    go.Bar(
        x = [max - min for min, max in zip(pasta_cooking['Cooking time (min)'],pasta_cooking['Cooking time (max)'])],
        y = pasta_cooking['Pasta'],
        orientation = 'h',
        width = 0.5
    )
)


fig.update_layout(
    barmode = 'stack'
)

fig.add_traces(
    go.Scatter(
        mode = 'markers',
        x = pasta_cooking['Cooking time (avg)'].tolist(),
        y = pasta_cooking['Pasta'],
        orientation = 'h',
        marker_symbol = 'line-ns',
        marker = dict(
            size = 20,
            line = dict(
                color = 'rgb(100,100,100)',
                width = 2
            )
        )
    )
)

fig.update_layout(
    showlegend = False,
    yaxis = dict(
        showgrid = False
    )
)

fig.write_image('./topics/059_pasta_cooking_time/data_processed/pasta_cooking_time.svg')
