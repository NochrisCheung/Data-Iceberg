from imdb import IMDb
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import visualisation_toolkit.chart_format_config as cfc

raw = pd.read_csv('./topics/083_henley_passport_index/data_processed/henley_passport_index_2020 - raw.csv')
henley_df = pd.DataFrame(raw[1::3],raw[2::3],raw[3::3])
clean_henley_df = pd.concat([raw[1::3].reset_index(drop = True),raw[2::3].reset_index(drop = True),raw[3::3].reset_index(drop = True)],axis=1)

clean_henley_df.to_csv('./topics/083_henley_passport_index/data_processed/henley_passport_index_2020 - cleaned.csv')

clean_henley_df.tail(30)
