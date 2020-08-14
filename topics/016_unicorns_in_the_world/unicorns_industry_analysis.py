import pandas as pd
import plotly.graph_objects as go

unicorn_df = pd.read_csv('./data_source/cb_insights/unicorns_in_the_world/unicorn_list.csv')

unicorn_df['Year Joined'] = pd.DatetimeIndex(unicorn_df['Date Joined']).year
unicorn_df.loc[426,'Industry'] = 'Edtech'
unicorn_industry_by_year = unicorn_df.groupby(by = ['Year Joined', 'Industry']).count().reset_index()
unicorn_industry_by_year = unicorn_industry_by_year.sort_values(by = ['Year Joined','Company'], ascending = False)
industry_list = unicorn_industry_by_year[unicorn_industry_by_year['Year Joined'] == 2019].sort_values(by = 'Company', ascending = False)['Industry'].unique().tolist()
# industry_list = unicorn_industry_by_year['Industry'].unique().tolist()
unicorn_df['Valuation ($B)'] = [v[1:] for v in unicorn_df['Valuation ($B)']]
unicorn_df = unicorn_df.astype({
    'Company' : str,
    'Valuation ($B)' : float,
    'Date Joined' : 'datetime64[ns]',
    'Country' : str,
    'Select Investors' : str,
    'Year Joined' : str
    }
)


unicorn_by_industry = unicorn_df.groupby(by = 'Industry').agg({
    'Company' : 'count',
    'Valuation ($B)' : 'sum',
    'Date Joined' : 'min',
    # 'Country' : 'count',
    # 'Select Investors' : 'count',
    # 'Year Joined' : 'min'
    }
).sort_values(by = 'Date Joined').reset_index()

unicorn_by_industry.sort_values(by = 'Company', ascending = False)

fig = go.Figure()
for ind in industry_list:
    fig.add_trace(
        go.Bar(
            name = ind,
            x = unicorn_industry_by_year[unicorn_industry_by_year['Industry'] == ind]['Year Joined'],
            y = unicorn_industry_by_year[unicorn_industry_by_year['Industry'] == ind]['Company']
        )
    )

fig.update_layout(barmode='stack')

unicorn_industry_by_year
