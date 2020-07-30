import plotly.graph_objects as go

def add_bar_chart(fig, x, y, color_val):
    # Input data to create a bar chart
    fig.add_trace(
        go.Bar(
            # name = 'Q'+str(i),
            x = tier_2_sponsor_by_quarter.index[1:],
            y = tier_2_sponsor_by_quarter.values[1:],
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
