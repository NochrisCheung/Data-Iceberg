import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

monopoly_df = pd.read_csv('./data_source/github/monopoly/monopolygame.csv')
only_street_df = monopoly_df.dropna()

roi_calculation = only_street_df[['name','color']]

for i in range(0,5):
    roi_calculation['roi_'+ str(i)] = round(only_street_df['rent_'+str(i)] /(only_street_df['cost'] + only_street_df['house_price'].mul(i)),4)


roi_calculation['roi_hotel'] = round(only_street_df['rent_hotel']/(only_street_df['cost'] + only_street_df['house_price'].mul(5)),4)
roi_calculation = roi_calculation.iloc[::-1]

color_dict = {
    'purple' : 'saddlebrown',
    'lightblue' : 'skyblue',
    'violet' : 'darkorchid',
    'orange' : 'orange',
    'red' : 'red',
    'yellow' : 'yellow',
    'darkgreen' : 'green',
    'darkblue' : 'blue'
 }

sum_width = roi_calculation.max()[2:].sum()
ind_width = roi_calculation.max()[2:]/sum_width
ind_width
fig = make_subplots(rows = 1, cols = 6,  column_widths = [0.07, 0.11, 0.12, 0.2, 0.20,0.30])
# roi_calculation.columns[2:].tolist()[::-1]
roi_list = roi_calculation.columns[2:].tolist()
for roi in roi_list:
    # roi_sorted = roi_calculation.sort_values(by = roi, ascending = True)
    fig.add_trace(
        go.Bar(
            x = roi_calculation[roi],
            y = roi_calculation['name'],
            marker = dict(
                # color = [color_dict[c] for c in roi_calculation['color']]
                color = roi_calculation[roi],
                colorscale = ['red','yellow','green'],
                # reversescale = True
                line = dict(
                    width = 0
                ),
            ),
            orientation = 'h',
            text = [str(round(100 * roi,1))+ '%' for roi in roi_calculation[roi]],
            textposition = 'outside',
            textfont_size = 10
        ),
        row = 1, col = 1 + roi_list.index(roi)
    )

fig.update_layout(
width = 700,
height = 700,
plot_bgcolor = 'aliceblue',
paper_bgcolor = 'aliceblue',
# template = 'simple_white')
)

fig.update_layout(
    margin=dict(
        l=90,
        r=60,
        b=60,
        t=240,
        pad = 5
    )
)

# Configure font
fig.update_layout(
    font = dict(
        size = 16,
        family = 'Oswald'
        )
)


fig.update_layout(
    showlegend = False,
    yaxis1 = dict(
        showline = False,
        showticklabels =False,
        zeroline = False,
        showdividers = False
    ),
    yaxis2 = dict(
        showline = False,
        showticklabels =False,
        zeroline = False,
        showdividers = False
    ),
    yaxis3 = dict(
        showline = False,
        showticklabels =False,
        zeroline = False,
        showdividers = False
     ),
    yaxis4 = dict(
        showline = False,
        showticklabels =False,
        zeroline = False,
        showdividers = False
    ),
    yaxis5 = dict(
        showline = False,
        showticklabels =False,
        zeroline = False,
        showdividers = False
    ),
    yaxis6 = dict(
        showline = False,
        showticklabels =False,
        zeroline = False,
        showdividers = False
    ),
    xaxis1 = dict(
        # gridwidth = 1,
        # gridcolor = 'lightsteelblue',
        range = [0, 1],
        showticklabels = False,
        showgrid = False,
        showline = False,
        zeroline = False,
    ),
    xaxis2 = dict(
        # gridwidth = 1,
        # gridcolor = 'lightsteelblue',
        range = [0, 1.6],
        showticklabels = False,
        showgrid = False,
        showline = False,
        zeroline = False,
    ),
    xaxis3 = dict(
        # gridwidth = 1,
        # gridcolor = 'lightsteelblue',
        range = [0, 1.6],
        showticklabels = False,
        showgrid = False,
        showline = False,
        zeroline = False,
    ),
    xaxis4 = dict(
        # gridwidth = 1,
        # gridcolor = 'lightsteelblue',
        range = [0, 2.1],
        showticklabels = False,
        showgrid = False,
        showline = False,
        zeroline = False,
    ),
    xaxis5 = dict(
        # gridwidth = 1,
        # gridcolor = 'lightsteelblue',
        range = [0, 2.1],
        showticklabels = False,
        showgrid = False,
        showline = False,
        zeroline = False,
    ),
    xaxis6 = dict(
        # gridwidth = 1,
        # gridcolor = 'lightsteelblue',
        range = [0, 2.1],
        showticklabels = False,
        showgrid = False,
        showline = False,
        zeroline = False,
    ),
)
fig.show()

fig.write_image('./topics/017_monopoly_analysis/data_processed/monopoly_street_roi.svg')
