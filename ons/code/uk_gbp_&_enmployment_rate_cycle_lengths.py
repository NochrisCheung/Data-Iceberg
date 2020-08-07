import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from visualisation_toolkit import chart_format_config as cfc

gdp_df = pd.read_csv('./ons/data_source/uk_gdp-030820.csv')
unemployment_df = pd.read_csv('./ons/data_source/uk_unemployment_rate-030820.csv')

start_period = '1977 Q1'
end_period = '2020 Q1'


# Process GDP data
gdp_by_quarter_df = gdp_df[gdp_df['Title'].str.contains('Q')]
gdp_by_quarter_df.columns = ['Period','GDP']
# gdp_by_quarter_df['GDP'] = [gdp * 1000000 for gdp in gdp_by_quarter_df['GDP'].values]
gdp_by_quarter_df.loc[:,'GDP']  = gdp_by_quarter_df.loc[:,'GDP'].astype('int').mul(1000000)
gdp_by_quarter_df = gdp_by_quarter_df.reset_index(drop = True)
gdp_period_index = gdp_by_quarter_df.index[(gdp_by_quarter_df['Period'] == start_period) | (gdp_by_quarter_df['Period'] == end_period)].tolist()
gdp_by_quarter_df.iloc[gdp_period_index[0]: gdp_period_index[1]]

gdp_by_quarter_df['Period'] = gdp_by_quarter_df['Period'].str.replace(' ', '-')
gdp_by_quarter_df['Period'] = pd.PeriodIndex(gdp_by_quarter_df['Period'].values, freq='Q').to_timestamp()
gdp_by_quarter_df[gdp_by_quarter_df['GDP'] >= gdp_by_quarter_df.iloc[212,1]].head(50)
gdp_by_quarter_df.iloc[97,1]
gdp_by_quarter_df.iloc[90:].head(50)

gdp_recovery_period = [12, 11, 21]

# Process unemployment rate data
unemployment_by_quarter_df = unemployment_df[unemployment_df['Title'].str.contains('Q')]
unemployment_by_quarter_df.columns = ['Period','Unemployment Rate']
unemployment_by_quarter_df['Employment Rate'] = unemployment_by_quarter_df.loc[:,'Unemployment Rate'].astype(float).sub(100).mul(-1)
unemployment_by_quarter_df = unemployment_by_quarter_df.reset_index(drop = True)
unemployment_period_index = unemployment_by_quarter_df.index[(unemployment_by_quarter_df['Period'] == start_period) | (unemployment_by_quarter_df['Period'] == end_period)].tolist()

unemployment_by_quarter_df['Period'] = unemployment_by_quarter_df['Period'].str.replace(' ', '-')
unemployment_by_quarter_df['Period'] = pd.PeriodIndex(unemployment_by_quarter_df['Period'].values, freq='Q').to_timestamp()

unemployment_by_quarter_df[unemployment_by_quarter_df['Employment Rate'] >= unemployment_by_quarter_df.iloc[150,2]].head(50)
unemployment_by_quarter_df.tail(50)

employment_rate_recovery_period = [44, 28, 31]

[sum(gdp_recovery_period)/len(gdp_recovery_period)]
[sum(employment_rate_recovery_period)/len(employment_rate_recovery_period)]

colorscale = ['lightskyblue','steelblue', 'navy', 'darkslateblue','indigo']

fig = make_subplots(specs = [[{'secondary_y': True}]])
cfc.configure_chart(fig)

fig.add_trace(
    go.Bar(
        name = 'Employement Rate',
        x = [float(em_rate) for em_rate in employment_rate_recovery_period] + [sum(employment_rate_recovery_period)/len(employment_rate_recovery_period)],
        y = [3, 2, 1, 0],
        orientation = 'h',
        # width = 0.3,
        marker = dict(
            # shape = 'spline',
            color = colorscale[4]
            # colorscale =
            # width = 3,
        )
    ),
)

fig.add_trace(
    go.Bar(
        name = 'GDP',
        x = [float(gdp) for gdp in gdp_recovery_period] + [sum(gdp_recovery_period)/len(gdp_recovery_period)],
        y = [3, 2, 1, 0],
        orientation = 'h',
        # width = 0.3,
        marker = dict(
            # shape = 'spline',
            color = colorscale[0]
            # colorscale =
            # width = 3,
        )
    ),
    # secondary_y = False
)


fig.update_layout(
    showlegend= False,
    xaxis=dict(
        showticklabels=True,
        zeroline = True,
        showgrid = True,
        dtick = 12,

        gridcolor = 'lightsteelblue',
        gridwidth = 1,

        zerolinecolor = 'lightsteelblue',

        range = [0, 49]
        ),
    yaxis = dict(
        type = 'linear',
        showline = False,
        showgrid = False,
        zeroline = False,
        showticklabels = False,
        ),
    # bargroupgap = 0
)

fig.update_layout(
    margin=dict(
        l=100,
        r=10,
        b=6 0,
        t=180,
        pad = 5
    )
)

fig.write_image('./ons/data_processed/uk_gdp_employment_rate_cycle_period.svg')
