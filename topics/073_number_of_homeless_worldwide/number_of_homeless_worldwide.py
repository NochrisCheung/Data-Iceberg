import pandas as pd
import plotly.graph_objects as go
import visualisation_toolkit.chart_format_config as cfc

homesless_df = pd.read_csv('./topics/073_number_of_homeless_worldwide/data_processed/number_of_homeless_in_wordwide - From website.csv')
homesless_df.columns

homesless_df = homesless_df.sort_values('Homeless as % of total population', ascending = False)

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

fig = cfc.configure_double_axes_chart()

fig.add_trace(
    go.Bar(
        x = homesless_df['Country'],
        y = homesless_df['Homeless as % of total population'],
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
        width = 0.7,
        text = [str(round(p*100,2))+'%' for p in homesless_df['Homeless as % of total population']],
        textposition = 'outside',
        textfont = dict( size = 20)
    ),
    secondary_y = False
)

fig.add_trace(
    go.Bar(
        x = homesless_df['Country'],
        y = homesless_df['Number of homeless'],
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
        width = 0.3,
        text = [str(round(p/1000,2)) for p in homesless_df['Number of homeless']],
        textposition = 'outside',
        textfont = dict(size = 20)
    ),
    secondary_y = True
)


fig.update_layout(
    showlegend = False,
    xaxis = dict(
        dtick = 1
    ),
    yaxis1 = dict(
        showgrid = False,
        showticklabels = True,
        tickformat = ',.1%'
    ),
    yaxis2 = dict(
        showgrid = False,
        showticklabels = True,
    )
)

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
    # )
fig.write_image('./topics/073_number_of_homeless_worldwide/data_processed/number_of_homeless_in_wordwide - From website.svg')
