import pandas as pd
import plotly.graph_objects as go
import visualisation_toolkit.chart_format_config as cfc

education_df = pd.read_csv('./topics/049_country_uni_education_quality/data_processed/Coursera - Unemploy vs Student Num.csv')
education_df.columns

fig = cfc.configure_chart()

fig.add_trace(
    go.Scatter(
        y = education_df['Unemployment %']/100,
        x = education_df['Student to Staff'],
        mode = 'markers+text',
        marker = dict(
            size = education_df['Number of Students']/100000,
            color = education_df['Unemployment %'],
             # + all_kcal_by_countries_filtered['Protein %'],
            opacity = 0.9,
            line_width = 0.5,
            line_color = '#2A3F5F',

            colorscale = 'Plasma',
            # colorbar = dict(
            #     thickness = 10,
            #     lenmode = 'pixels',
            #     len = 420,
            #     dtick = 0.1,
            #     yanchor = 'middle',
            #     tickformat = '%',
            # ),
        ),

        text = education_df['GEO'],
        # text = [country if country in label_list else '' for country in all_kcal_by_countries_filtered['Countries']],
        textfont_size = 10,
    ),
)

fig.update_traces(textposition='middle right')

fig.update_layout(
    showlegend= False,
    xaxis=dict(
        showticklabels=True,
        zeroline = False,
        showgrid = False,
        dtick = 10,
        # tickformat = '%',

        ticks = 'inside',
        tickwidth = 1,
        ticklen = 7,
        tickcolor='#2A3F5F',

        range = [0, 50.1]
        ),
    yaxis = dict(
        type = 'linear',
        showline = False,
        showgrid = False,
        zeroline = False,
        showticklabels = True,
        dtick = 0.04,
        tickformat = '%',

        ticks = 'inside',
        tickwidth = 1,
        ticklen = 7,
        tickcolor='#2A3F5F',

        range = [0, 0.121]
        ),
    # bargroupgap = 0
)

fig.update_layout(
    margin=dict(
        l=60,
        r=40,
        b=70,
        t=190,
        pad = 5
    )
)
fig.show()
fig.to_image(engine = 'kaleido')
fig.write_image('./topics/049_country_uni_education_quality/data_processed/university_education_quality.svg')
