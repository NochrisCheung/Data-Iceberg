import pandas as pd
import numpy as np
import plotly.graph_objects as go
import visualisation_toolkit.chart_format_config as cfc
import json
from datetime import datetime
from collections import Counter

data = json.load(open('analytics/data_iceberg_20201109/likes.json'))
data['media_likes']

likes = pd.DataFrame(data['media_likes'], columns = ['time','account'])
likes['time'] = likes['time'].astype('datetime64[ns]')
likes['account'] = likes['time'].astype('string')
likes
hours = [t.time().hour for t in likes['time']]

Counter(hours).keys()
Counter(hours).values()

like_time = pd.DataFrame([Counter(hours).keys(),Counter(hours).values()]).transpose()
like_time.columns = ['hours','count']
like_time = like_time.sort_values('hours')
like_time

fig = cfc.configure_chart()

fig.add_trace(
    go.Bar(
        x = like_time['hours'],
        y = like_time['count']
    )
)

fig.update_layout(
    xaxis = dict(
        dtick = 1
    )
)

likes
