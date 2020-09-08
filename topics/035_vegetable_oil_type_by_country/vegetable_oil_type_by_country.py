import pandas as pd
import plotly.graph_objects as go
import visualisation_toolkit.chart_format_config as cfc
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
import numpy as np

food_balance_df = pd.read_csv('./data_source/faostat/food_balance/FoodBalanceSheets_E_All_Data.csv', encoding = 'ISO-8859-1')

include_list = [
    'Asia',
    'Africa',
    'Europe',
    'Northern America',
    'Oceania',
    'South America',
    'World',
    ]

food_balance_df['Item'].unique()

oil_source = food_balance_df[(food_balance_df['Area'].isin(include_list)) & ([' oil' in item.lower() for item in food_balance_df['Item']])]

oil_source.head(50)
oil_source_by_country = oil_source[oil_source['Element'] == 'Food'].pivot_table(values = 'Y2017', index = 'Item', columns = 'Area', aggfunc = 'sum', fill_value = 0).reset_index()
oil_source_by_country = oil_source_by_country.sort_values(by = 'World', ascending = False).reset_index(drop = True)
oil_source_by_country
oil_source_by_country_filtered = oil_source_by_country[1:5].append(oil_source_by_country[6:11]).reset_index(drop = True)
oil_source_by_country_filtered.loc[10]
oil_source_by_country_filtered
oil_source_by_country_filtered.loc[10] = ['Other oil'] + [x - y for x, y in zip(oil_source_by_country.iloc[0,1:], oil_source_by_country_filtered.sum()[1:])]
for col in oil_source_by_country_filtered.columns[1:]:
    oil_source_by_country_filtered[col] = oil_source_by_country_filtered[col].transform(lambda x: x / x.sum())

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
    '150,150,150'
]

fig = cfc.configure_chart()

i = 0
for oil in oil_source_by_country_filtered['Item'].unique():
    oil_df = oil_source_by_country_filtered[oil_source_by_country_filtered['Item'] == oil]
    [values] = oil_df.iloc[:,1:].values.tolist()
    fig.add_traces(
        go.Bar(
            name = oil,
            x = oil_df.columns[1:],
            y = values,
            marker = dict(
                color = 'rgb(' + color_scheme[i] +')'
            )
        )
    )
    i = i + 1

fig.update_layout(
    barmode='stack',
    showlegend = False,
    yaxis = dict(
        tickformat = '%'
    )
)

fig.show()

fig.write_image('./topics/035_vegetable_oil_type_by_country/data_processed/vegetable_oil_type_by_country.svg')
