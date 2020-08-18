import pandas as pd
import numpy as np
import plotly.graph_objects as go
import visualisation_toolkit.chart_format_config as cfc
from sklearn.cluster import KMeans

whisky_df = pd.read_csv('./data_source/selfbuilt_whisky_analysis/whisky_database/Meta-Critic Whisky Database – Selfbuilts Whisky Analysis.csv')


whisky_df.columns

whisky_df['Super Cluster'].unique()
whisky_df['Cluster'].unique()
fig = cfc.configure_chart()

fig.add_trace(
    go.Scatter(
        x = np.arange(1,7),
        y = whisky_df.groupby('Cost')['Meta Critic'].median().to_list(),
        mode = 'markers'

    )
)




X = whisky_df[['Meta Critic','Cost','Class','Country','Type']]
X
X['Cost'] = [len(str(c)) for c in X['Cost']]
class_list = X['Class'].unique().tolist()
X['Class'] = [class_list.index(c) for c in X['Class']]
country_list = X['Country'].unique().tolist()
X['Country'] = [country_list.index(c) for c in X['Country']]
type_list = X['Type'].unique().tolist()
X['Type'] = [type_list.index(t) for t in X['Type']]

X

kmeans = KMeans(n_clusters = 5, random_state = 0).fit(X)

kmeans.labels_

fig = cfc.configure_chart()

fig.add_traces(
    go.Scatter(
        # x =  X['Country'],
        # x = [country_list[c] for c in X['Country']],
        # x = [class_list[c] for c in X['Class']],
        # x = X['Cost'],
        x = [type_list[t] for t in X['Type']],
        y = X['Meta Critic'],
        mode = 'markers',
        marker = dict(
            color = kmeans.labels_
        )
    )
)
X['Meta Critic']
X['Country']
