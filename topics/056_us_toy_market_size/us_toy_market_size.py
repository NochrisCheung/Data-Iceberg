import pandas as pd
import plotly.graph_objects as go
import visualisation_toolkit.chart_format_config as cfc

toy_df = pd.read_csv('./topics/056_us_toy_market_size/data_processed/us_toy_market_size_by_category - market_size.csv', index_col= 0)
toy_df = toy_df.sort_values(by = '2017', ascending = True)
fig = cfc.configure_chart()


def f(x):
    return x[1]-x[0] -1
toy_df
[y/x-1 for x, y in zip(toy_df['2017'],toy_df['2019'])]

i = 1
for year in toy_df[['2017','2019']].columns:
    fig.add_trace(
        go.Scatter(
            y = toy_df.index.tolist(),
            x = [i]*11,
            mode = 'markers+text',
            marker = dict(
                size = toy_df[year].apply(lambda x: x*10).tolist(),
                # color = education_df['Unemployment %'],
                 # + all_kcal_by_countries_filtered['Protein %'],
                opacity = 0.9,
                line_width = 0.5,
                line_color = '#2A3F5F',

                # colorscale = 'Plasma',
                # colorbar = dict(
                #     thickness = 10,
                #     lenmode = 'pixels',
                #     len = 420,
                #     dtick = 0.1,
                #     yanchor = 'middle',
                #     tickformat = '%',
                # ),
            ),

            text = toy_df[year].tolist(),
            # text = [country if country in label_list else '' for country in all_kcal_by_countries_filtered['Countries']],
            textfont_size = 10,
        ),
    )
    i = i +1

fig.show()
fig.update_traces(textposition='middle right')

fig.update_layout(
    showlegend= False,
    xaxis=dict(
    #     showticklabels=True,
    #     zeroline = False,
    #     showgrid = False,
        dtick = 1,
    #     # tickformat = '%',
    #
    #     ticks = 'inside',
    #     tickwidth = 1,
    #     ticklen = 7,
    #     tickcolor='#2A3F5F',
    #
        range = [0, 2.5]
        ),
    yaxis = dict(
        # type = 'linear',
        showline = False,
        showgrid = False,
        zeroline = False,
        showticklabels = True,
        # dtick = 0.04,
        # tickformat = '%',

        ticks = 'inside',
        tickwidth = 0,
        ticklen = 0,
        tickcolor='#2A3F5F',

        # range = [0, 0.121]
        ),
    # bargroupgap = 0
)

fig.update_layout(
    margin=dict(
        l=80,
        r=60,
        b=70,
        t=190,
        pad = 5
    )
)
fig.show()
fig.to_image(engine = 'kaleido')
fig.write_image('./topics/056_us_toy_market_size/data_processed/us_toy_market_size_by_category.svg')
