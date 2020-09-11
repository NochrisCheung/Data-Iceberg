import pandas as pd
import plotly.graph_objects as go
import visualisation_toolkit.chart_format_config as cfc

country_df = pd.read_csv('./data_source/cbs/first_time_mother/mean_age_of_first_time_mother_in_EU.csv')
country_df = country_df[:-1][::-1]
country_df
country_df.iloc[:,0]

birth_2013 = country_df['2013 (yrs)']
birth_2017 = country_df['2017 (yrs)']

fig = cfc.configure_chart()

fig.add_trace(
    go.Bar(
        name = '2017',
        x = birth_2017,
        y = country_df.iloc[:,0],
        orientation = 'h',
        marker = dict(
            # color = [condiment_df['Condiment'].ne(c).idxmin() for c in condiment_df['Condiment'].iloc[::-1]],
            # color = ['rgb('+c+')' for c in color_scheme[0:8]],
            color = 'indigo',
            # opacity = 0.9,
            # line = dict(
                # color = [condiment_df['Condiment'].ne(c).idxmin() for c in condiment_df['Condiment'].iloc[::-1]],
                # color = ['rgb('+c+')' for c in color_scheme[0:8]]
                # colorscale = ['lightskyblue','steelblue', 'navy'],
            # )
        ),
        width = 0.4
    )
)

fig.add_trace(
    go.Bar(
        name = '2013',
        x = birth_2013,
        y = country_df.iloc[:,0],
        orientation = 'h',
        marker = dict(
            # color = [condiment_df['Condiment'].ne(c).idxmin() for c in condiment_df['Condiment'].iloc[::-1]],
            # color = ['rgb('+c+')' for c in color_scheme[0:8]],
            color = 'steelblue',
            # opacity = 0.9,
            # line = dict(
                # color = [condiment_df['Condiment'].ne(c).idxmin() for c in condiment_df['Condiment'].iloc[::-1]],
                # color = ['rgb('+c+')' for c in color_scheme[0:8]]
                # colorscale = ['lightskyblue','steelblue', 'navy'],
        ),
        # ),
        width = 0.4
    ),
)



fig.update_layout(

    xaxis = dict(
        zeroline = False,
        showticklabels = True,
        showgrid = True,
        gridcolor = 'lightsteelblue',
        range = [25,31.1],
        dtick = 1
    ),
    yaxis = dict(
        zeroline = False,
        showgrid = False,
        showticklabels = True,
        dtick = 1
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
fig.write_image('./topics/041_first_time_mother/data_processed/mean_age_of_first_time_mother_in_EU.svg')
