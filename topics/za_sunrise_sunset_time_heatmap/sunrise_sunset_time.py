import pandas as pd
import numpy as np
import plotly.graph_objects as go
import visualisation_toolkit.chart_format_config as cfc

sun_df = pd.read_excel('./topics/za_sunrise_sunset_time_heatmap/data_processed/day_length.xlsx',sheet_name = 'Sunrise Sunset')
