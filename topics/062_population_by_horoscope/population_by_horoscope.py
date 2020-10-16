import pandas as pd
import plotly.graph_objects as go
import visualisation_toolkit.chart_format_config as cfc

horoscope_df = pd.read_csv('./topics/062_population_by_horoscope/data_processed/world_population_by_horoscope - count.csv')
horoscope_df['%'] = horoscope_df['count']/horoscope_df['count'].sum()
horoscope_df = horoscope_df.sort_values(by = 'month', ascending= False)
horoscope_df

fig = cfc.configure_chart()

fig.add_trace(
    go.Bar(
        x = horoscope_df['%'],
        y = horoscope_df['horoscope'],
        orientation = 'h',
        # marker = dict(
            # color = [condiment_df['Condiment'].ne(c).idxmin() for c in condiment_df['Condiment'].iloc[::-1]],
            # color = ['rgb('+c+')' for c in color_scheme[0:8]],
            # colorscale = ['lightskyblue','steelblue', 'navy'],
            # opacity = 0.9,
            # line = dict(
                # color = [condiment_df['Condiment'].ne(c).idxmin() for c in condiment_df['Condiment'].iloc[::-1]],
                # color = ['rgb('+c+')' for c in color_scheme[0:8]]
                # colorscale = ['lightskyblue','steelblue', 'navy'],
            # )
        # ),
        width = 0.5,
        text = [str(p*100)[0:3]+'%' for p in horoscope_df['%']],
        textposition = 'outside',
        textfont = dict( size = 16)
    )
)

fig.update_layout(
    xaxis = dict(
        showticklabels = False,
        range = [0,0.12]
    ),
    yaxis = dict(
        showgrid = False,
        showticklabels = True
    )
)
    #
    # fig.update_layout(
    #     margin=dict(
    #         l=90,
    #         r=90,
    #         b=40,
    #         t=200,
    #         pad = 5
    #     )
    # )
fig.write_image('./topics/062_population_by_horoscope/data_processed/world_population_by_horoscope.svg')
