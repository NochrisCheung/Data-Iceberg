import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from visualisation_toolkit import chart_format_config as cfc

gdp_df = pd.read_csv('./ons/data_source/uk_gdp-030820.csv')
unemployment_df = pd.read_csv('./ons/data_source/uk_unemployment_rate-030820.csv')

start_period = '2006 Q1'
end_period = '2016 Q4'


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

# Process unemployment rate data
unemployment_by_quarter_df = unemployment_df[unemployment_df['Title'].str.contains('Q')]
unemployment_by_quarter_df.columns = ['Period','Unemployment Rate']
unemployment_by_quarter_df['Employment Rate'] = unemployment_by_quarter_df.loc[:,'Unemployment Rate'].astype(float).sub(100).mul(-1)
unemployment_by_quarter_df = unemployment_by_quarter_df.reset_index(drop = True)
unemployment_period_index = unemployment_by_quarter_df.index[(unemployment_by_quarter_df['Period'] == start_period) | (unemployment_by_quarter_df['Period'] == end_period)].tolist()

unemployment_by_quarter_df['Period'] = unemployment_by_quarter_df['Period'].str.replace(' ', '-')
unemployment_by_quarter_df['Period'] = pd.PeriodIndex(unemployment_by_quarter_df['Period'].values, freq='Q').to_timestamp()


colorscale = ['lightskyblue','steelblue', 'navy', 'darkslateblue','indigo']
fig = make_subplots(specs = [[{'secondary_y': True}]])
cfc.configure_chart(fig)

fig.add_trace(
    go.Scatter(
        name = 'GDP',
        x = gdp_by_quarter_df.iloc[gdp_period_index[0]: gdp_period_index[1]]['Period'],
        y = gdp_by_quarter_df.iloc[gdp_period_index[0]: gdp_period_index[1]]['GDP'],
        mode = 'lines',
        line = dict(
            shape = 'spline',
            color = colorscale[0],
            width = 3,
        )
    ),
    secondary_y = False
)

fig.add_trace(
    go.Scatter(
        name = 'Employement Rate',
        x = unemployment_by_quarter_df.iloc[unemployment_period_index[0]: unemployment_period_index[1]]['Period'],
        y = unemployment_by_quarter_df.iloc[unemployment_period_index[0]: unemployment_period_index[1]]['Employment Rate'],
        mode = 'lines',
        line = dict(
            shape = 'spline',
            color = colorscale[4],
            width = 3,
        )
    ),
    secondary_y = True
)

fig.update_layout(
    showlegend= False,
    xaxis=dict(
        showticklabels=True
        ),
    yaxis1=dict(
        type='linear',
        range=[419.8*10**9, 504*10**9],
        dtick = 20*10**9
        ),
    yaxis2 = dict(
        type = 'linear',
        range = [90.98, 95.18],
        dtick = 1,
        showline = False,
        showgrid = False,
        zeroline = False,
        showticklabels=True
        )
)

fig.update_layout(
    margin=dict(
        l=60,
        r=10,
        b=60,
        t=180,
        pad = 5
    )
)

fig.write_image('./ons/data_processed/uk_gdp_employment_rate_2008_to_2013.svg')
