import pandas as pd
import plotly.graph_objects as go
import visualisation_toolkit.chart_format_config as cfc

restaurant_df = pd.read_csv('./topics/074_covid_restaurant_recovery/data_processed/YoY_Seated_Diner_Data.csv')

country_df = restaurant_df[restaurant_df['Type'] == 'country']

transposed_country_df = country_df.set_index('Name', drop = True).iloc[:,1:].transpose()
transposed_country_df.mask(transposed_country_df != 0).reset_index(drop = True).apply(pd.Series.first_valid_index, 0).head(50)

usable_df = transposed_country_df[15:]

color_scheme = [
    '65,105,225',
    '127,255,212',
    '144,238,144',
    '240,230,140',
    '255,160,122',
    '205,92,92',
    '219,112,147',
    '186,85,211',
    '147,112,219',
    '33,33,33'
]


fig = cfc.configure_chart()

colorscale = ['lightskyblue','steelblue', 'navy', 'darkslateblue','indigo']
i = 0
for col in usable_df:
    line_setting = dict(
        shape = 'spline',
        color = 'rgb('+color_scheme[i]+')',
        width = 3,
    )
    fig.add_trace(
        go.Scatter(
            name = col,
            x = usable_df.index,
            y = usable_df[col].values/100,
            mode = 'lines',
            line = line_setting

        ),
    )
    i = i + 1

fig.update_layout(
    width = 1400,
    margin=dict(
        l=52,
        r=12,
        b=60,
        t=180,
        pad = 5
    )
)


fig.update_layout(
    showlegend = True,
    # xaxis = dict(
    #     dtick = 1
    # ),
    yaxis = dict(
        showgrid = False,
        showticklabels = True,
        tickformat = ',.0%'
    )
)

fig.write_image('./topics/074_covid_restaurant_recovery/data_processed/YoY_Seated_Diner_Data.svg')
