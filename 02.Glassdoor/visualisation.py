import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import os

mydir = '/Users/nochris/Documents/Culture'

glassdoor_grades_df = pd.read_csv(mydir +'/ftse100/ftse100_glassdoor_grades_cleaned.csv')
glassdoor_grades_df.columns = ['index','company_name','rating','review_count','used_review','used_review_%','common_name','website','industry']

fig = go.Figure()

# Plot the scatter graph with data
fig.add_trace(
    go.Scatter(
        x = glassdoor_grades_df['rating'],
        y = glassdoor_grades_df['review_count'],
        # text = [cn if rc>=4000 else '' for cn, rc in zip(glassdoor_grades_df['common_name'],glassdoor_grades_df['review_count'])]
    )
)


# Define the marker format
fig.update_traces(
    mode='markers+text',
    marker = dict(
        line_width=1,
        size=12,
        color=glassdoor_grades_df['rating'],
        colorscale = 'Plasma'
    ),
    textposition='middle left'
)

fig.update_layout(
    shapes=[
        dict(
            type= 'line',
            yref= 'y',
            y0= 0,
            y1= 14500,
            xref= 'x',
            x0= glassdoor_grades_df['rating'].mean(),
            x1= glassdoor_grades_df['rating'].mean()
        )
    ]
)




#  Define the graph layout
fig.update_layout(
    width = 500,
    height = 500,
    plot_bgcolor = 'aliceblue',
    paper_bgcolor = 'aliceblue',
    # template = 'simple_white')
)

# Define titles
fig.update_layout(
    # title='Most FTSE100 employees are moderately <br >satisfied with their work environment',
    # xaxis_title = 'Glassdoor Rating',
    # yaxis_title = 'Number of Reviews',
    font = dict(
        family = 'Rockwell',
        size = 12,
        color = 'navy'
    )
)

# Confiure text font
fig.update_layout(
    titlefont = dict(
        color = 'darkslateblue',
        size = 23
    )
)

# Definte x-axis and y-axis layout
fig.update_layout(
    xaxis = dict(
        showline = False,
        showgrid = False,
        zeroline = False,

        tickmode = 'linear',
        range = [2, 5.1],
        dtick = 0.5,

        titlefont = dict(
            size = 12
        )
    ),
    yaxis = dict(
        showline = False,
        showgrid = True,
        zeroline = False,

        tickmode = 'linear',
        range = [-500, 14500],
        dtick = 2000,

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
    )
)

pio.orca.config.executable = '/usr/local/lib/python3.7/site-packages/orca'
pio.orca.config.save()
fig.write_image(mydir+'/image.png')
