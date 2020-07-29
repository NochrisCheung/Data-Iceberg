import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
pio.kaleido.scope.default_format = 'png'

mydir = '/Users/nochris/Documents/Job_Market'


sponsor_df = pd.read_csv(mydir + '/UKTiersponsors_All.csv')

sponsor_df['Date Added'] = pd.to_datetime(sponsor_df['Date Added'])
sponsor_by_tier_type_by_month = sponsor_df.pivot_table(values = 'Town', index= 'Date Added', columns = 'Main Tier', aggfunc = 'count').groupby(pd.Grouper(freq = 'q', closed = 'left',label = 'left')).sum()

tier_2_columns = [col for col in sponsor_by_tier_type_by_month.columns if 'Tier 2' in col]
tier_2_sponsor_by_quarter = sponsor_by_tier_type_by_month[tier_2_columns].sum(axis = 1)


fig = go.Figure()

# for i in range(2014, 2021):
#     fig.add_trace(
#         go.Bar(
#             name = i,
#             x = ['Q1','Q2','Q3','Q4'],
#             y = [val for ind, val in zip(tier_2_sponsor_by_quarter.index, tier_2_sponsor_by_quarter.values) if ind.year == i]
#         )
#     )
# i=1
#
# for i in range(1,5):
#     fig.add_trace(
#         go.Bar(
#             name = 'Q'+str(i),
#             x = tier_2_sponsor_by_quarter.index[1+i::4],
#             y = tier_2_sponsor_by_quarter.values[1+i::4]
#
#         )
#     )

fig.add_trace(
    go.Bar(
        # name = 'Q'+str(i),
        x = tier_2_sponsor_by_quarter.index[1:],
        y = tier_2_sponsor_by_quarter.values[1:],
    )
)

# Confiure text font
fig.update_layout(
    titlefont = dict(
        color = 'darkslateblue',
        size = 23
    )
)

fig.update_traces(
    marker = dict(
        color= tier_2_sponsor_by_quarter.index[1:].values,
        # colorscale = 'Plasma'
        colorscale = ['lightskyblue','steelblue', 'navy', 'darkslateblue','indigo'],
        reversescale= False
    )
    # textposition='middle left'
)

#  Define the graph layout
fig.update_layout(
    width = 500,
    height = 500,
    plot_bgcolor = 'aliceblue',
    paper_bgcolor = 'aliceblue',
    # template = 'simple_white')
)

# Definte x-axis and y-axis layout
fig.update_layout(
    xaxis = dict(
        showline = False,
        showgrid = False,
        zeroline = False,
        titlefont = dict(
            size = 12
        )
    ),
    yaxis = dict(
        showline = False,
        showgrid = True,
        zeroline = False,

        gridwidth = 1,
        gridcolor = 'lightsteelblue',

        titlefont = dict(
            size = 12
        )
    )
)

fig.update_layout(
    margin=dict(
        l=30,
        r=30,
        b=40,
        t=150,
        pad = 5
    )
)

fig.to_image(engine = 'kaleido')
fig.write_image(mydir + '/image.png')
