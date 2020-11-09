import pandas as pd
import plotly.graph_objects as go
import visualisation_toolkit.chart_format_config as cfc

vote_df = pd.read_csv('./topics/084_us_electoral_votes_per_states/data_processed/us_electoral_votes - population.csv')
vote_df_cleaned.columns
vote_df_cleaned = vote_df.iloc[:,0:4]
vote_df_cleaned

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
        x = vote_df_cleaned['States'],
        y = vote_df_cleaned['Census population 2019'],
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
        text = [str(round(p/1000000,1))+'M' for p in vote_df_cleaned['Census population 2019']],
        textposition = 'outside',
        textfont = dict( size = 20)
    ),
    secondary_y = False
)

fig.add_trace(
    go.Bar(
        x = vote_df_cleaned['States'],
        y = vote_df_cleaned['Electoral votes'],
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
        text = vote_df_cleaned['Electoral votes'],
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
        # tickformat = ',.1%'
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
fig.write_image('./topics/084_us_electoral_votes_per_states/data_processed/us_electoral_votes - population.svg')
