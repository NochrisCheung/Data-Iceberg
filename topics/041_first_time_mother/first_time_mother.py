import pandas as pd
import plotly.graph_objects as go
import visualisation_toolkit.chart_format_config as cfc

age_group_df = pd.read_csv('./data_source/cbs/first_time_mother/first_born_child_by_age_of_mother.csv')
age_group_df = age_group_df[::-1]
age_group_df.iloc[:,0]

birth_2008 = age_group_df['2008 (x 1,000)']/age_group_df['2008 (x 1,000)'].sum()
birth_2018 = age_group_df['2018 (x 1,000)']/age_group_df['2018 (x 1,000)'].sum()

fig = cfc.configure_chart()

fig.add_trace(
    go.Bar(
        name = '2018',
        x = birth_2018,
        y = age_group_df.iloc[:,0],
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
        text = ['{:.1%}'.format(b) for b in birth_2018],
        textposition = 'outside',
        width = 0.4
    )
)

fig.add_trace(
    go.Bar(
        name = '2008',
        x = birth_2008,
        y = age_group_df.iloc[:,0],
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
        text = ['{:.1%}'.format(b) for b in birth_2008],
        textposition = 'outside',
        # ),
        width = 0.4
    ),
)

fig.update_layout(

    xaxis = dict(
        showticklabels = False
    ),
    yaxis = dict(
        zeroline = False,
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
fig.write_image('./topics/041_first_time_mother/data_processed/first_born_child_by_age_of_mother.svg')
