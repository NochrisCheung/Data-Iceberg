import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio

def configure_chart():
    #  Define the graph layout
    fig = go.Figure()

    fig.update_layout(
        width = 700,
        height = 700,
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
        ),
        yaxis = dict(
            showline = False,
            showgrid = True,
            zeroline = False,

            gridwidth = 1,
            gridcolor = 'lightsteelblue',
        )
    )

    fig.update_layout(
        margin=dict(
            l=60,
            r=30,
            b=60,
            t=180,
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

    return fig

def configure_double_axes_chart():
    #  Define the graph layout
    fig = make_subplots(specs = [[{'secondary_y': True}]])

    fig.update_layout(
        width = 700,
        height = 700,
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
        ),
        yaxis1 = dict(
            showline = False,
            showgrid = True,
            zeroline = False,

            gridwidth = 1,
            gridcolor = 'lightsteelblue',
        ),
        yaxis2 = dict(
            showline = False,
            showgrid = True,
            zeroline = False,

            gridwidth = 1,
            gridcolor = 'lightsteelblue',
        )
    )

    fig.update_layout(
        margin=dict(
            l=60,
            r=30,
            b=60,
            t=180,
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

    return fig
