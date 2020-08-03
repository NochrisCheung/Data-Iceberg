import google_trend.code.google_trend_scraper as gts
from pytrends.request import TrendReq
import plotly.graph_objects as go
import visualisation_toolkit.chart_format_config as cfc

pytrends = TrendReq(hl='en-UK', tz=360,  timeout=(10,25))
pytrends.build_payload(['Shake It Off','I Knew You Were Trouble','Blank Space','Love Story','I Don’t Wanna Live Forever (Fifty Shades Darker)'], cat= 35, timeframe='all', geo = '')
data = pytrends.interest_over_time()
data


fig = go.Figure()
cfc.configure_chart(fig)

for search_term in data.columns[0:-1]:
    fig.add_trace(
        go.Scatter(
            name = search_term,
            x = data[search_term].index,
            y = data[search_term].values
        )
    )

fig.show()
