import pandas as pd
import numpy as np
import plotly.graph_objects as go
import visualisation_toolkit.chart_format_config as cfc

nutrient_df = pd.read_csv('./topics/066_food_nutrient_composition/data_processed/food_calorie_list - calorie.csv')
nutrient_df.columns
nutrient_df[['Food','Fat (g)','Carbohydrates (g)','Fibre (g)','Protein (g)','Salt (g)']]

nutrient_df[['Food','Fat (g)','Carbohydrates (g)','Fibre (g)','Protein (g)','Salt (g)']].sum(axis= 1)


new_nutrient_df = pd.DataFrame()

new_nutrient_df['Unsaturated Fat'] = nutrient_df['Fat (g)'] - nutrient_df['of which saturates (g)']
new_nutrient_df['Saturated Fat'] = nutrient_df['of which saturates (g)']
new_nutrient_df['Carbohydrates'] = nutrient_df['Carbohydrates (g)'] - nutrient_df['of which sugars (g)']
new_nutrient_df['Sugar'] = nutrient_df['of which sugars (g)']
new_nutrient_df[['Fibre','Protein','Salt']] = nutrient_df[['Fibre (g)', 'Protein (g)', 'Salt (g)']]

new_nutrient_pc_df = new_nutrient_df.div(new_nutrient_df.sum(axis=1), axis = 0)
new_nutrient_pc_df['Food'] = nutrient_df['Food']

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
new_nutrient_pc_df.columns[:-1]

fig = cfc.configure_chart()
i = 0
for cat in new_nutrient_pc_df.columns[:-1]:
    fig.add_trace(
        go.Bar(
            name = cat,
            x = new_nutrient_pc_df['Food'],
            y = new_nutrient_pc_df[cat],
            # mode = 'lines',
            marker = dict(
                color = 'rgbA('+color_scheme[i]+',1)',
                line = dict(
                    # shape = 'spline',
                    width = 0.3,
                    # color = 'rgb('+color_scheme[i]+')',
                    color = 'rgb(33,33,33)',
                ),
            )
            # line = dict(
            #     shape = 'spline',
            #     width = 3,
            #     color = 'rgb('+color_scheme[i]+')',
            # ),
            # fillcolor = 'rgba('+color_scheme[i]+',0.8)',
            # stackgroup = 'field',
            # barmode = 'stack'
            )
    )
    i = i +1

fig.update_layout(
    barmode = 'stack'
)

fig.update_layout(
    showlegend = True,
    xaxis = dict(
        showticklabels = False
        # range = [1988, 2018],
        # dtick = 5
         # tickmode = 'array',
         # tickvals = [0,1,2,3,4,5,6,7],
         # ticktext = ['1988', '1993','1998','2003','2008','2013','2018']
         # tick0 = 1988,
         # dtick = 5
    ),
    yaxis = dict(
        showgrid = False,
        tickformat = '%'
    )
)



fig.write_image('./topics/066_food_nutrient_composition/data_processed/food_nutrient_list.svg')
