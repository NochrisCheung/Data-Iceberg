import pandas as pd
import plotly.graph_objects as go
import visualisation_toolkit.chart_format_config as cfc

delay_df = pd.read_csv('./topics/za_london_underground_operations/data_processed/ldr_delay_time - delay.csv')

delay_df

london_tube_colors = {
'Bakerloo' : '#B36305',
'Central' : '#E32017',
'Circle & Ham' : '#FFD300',
'District' : '#00782A',
# 'Hammersmith and City	#F3A9BB	#CC9999
'Jubilee' : '#A0A5A9',
'Metropolitan' : '#9B0056',
'Northern' : '#000000',
'Piccadilly' : '#003688',
'Victoria' : '#0098D4',
'Waterloo & City' : '#95CDBA',
'All Line Combined' : '#123456'
}

fig = cfc.configure_chart()

for line  in delay_df.columns[1:]:
    fig.add_traces(
        go.Scatter(
            name  = line,
            mode = 'lines',
            x = delay_df['Unnamed: 0'][0:-1],
            y = delay_df[line][0:-1],
            line = dict(
                # shape = 'spline',
                color = london_tube_colors[line],
                width = 7
            )
        )
    )
fig.update_layout(
    showlegend = False,
    xaxis = dict(
        dtick = 2
    ),
    yaxis = dict(
        range = [0 , 2],
        dtick = 0.5,
        zeroline = True,
        zerolinecolor = 'lightsteelblue'

    ),
    margin=dict(
        l=60,
        r=100,
        b=60,
        t=200,
        pad = 5
    )
)

fig.show()

fig.write_image('./topics/za_london_underground_operations/data_processed/london_underground_delay.svg')
