import pandas as pd
import numpy as np
import plotly.graph_objects as go
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import visualisation_toolkit.chart_format_config as cfc

def func(x, a, b, c):
    return a * np.exp(b*x)+c


human_pop_df = pd.read_csv('data_source/united_state_census_bureau/human_population_evolution/human_population_evolution_in_millions.csv')
human_pop_before_1950_df = human_pop_df[['Year','Summary']][1:]
human_pop_before_1950_df['year_translated']= [-int(year.split(' ')[0]) if 'BC' in year else int(year.split(' ')[0]) for year in human_pop_before_1950_df['Year']]
human_pop_before_1950_df['Summary'] = human_pop_before_1950_df['Summary'].str.replace(',','').astype('float')
# human_pop_before_1950_df['year_translated'] = human_pop_before_1950_df['year_translated'].astype('float')
human_pop_before_1950_df.dtypes

human_pop_before_1950_df

human_pop_before_1950_df['year_translated'].transform(lambda x: np.log(x + 11950))
human_pop_before_1950_df['year_translated'][-5::].transform(lambda x: np.log(x + 10001)),
human_pop_before_1950_df['year_translated'][5::].transform(lambda x: np.log(x + 10001))
human_pop_before_1950_df['year_translated'][10::]
human_pop_before_1950_df['year_translated'][12::].transform(lambda x: np.log(x))
popt, pcov = curve_fit(func, human_pop_before_1950_df['year_translated'][12::].transform(lambda x: np.log(x)), human_pop_before_1950_df['Summary'][12::])
popt, pcov

x = human_pop_before_1950_df['year_translated'].values
y = human_pop_before_1950_df['Summary'].values

z = np.polyfit(x, y, 2)
f = np.poly1d(z)
y_new = f(x)
plt.plot(x,y,'o', x, y_new)

xx = np.linspace(1,1950, 1950)
xx
yy = func(np.log(xx), *popt)
yy
print(popt)
, pcov
fig = go.Figure()
cfc.configure_chart(fig)

fig.add_trace(
    go.Scatter(
        x = human_pop_before_1950_df['year_translated'][6::],
        y = human_pop_before_1950_df['Summary'][6::],
        mode = 'lines'
    )
)
human_pop_before_1950_df
