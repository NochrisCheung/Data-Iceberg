import pandas as pd
import plotly.graph_objects as go
import visualisation_toolkit.chart_format_config as cfc

london_underground_scheduled_km_df = pd.read_excel('./data_source/tfl/operated_km/lu-performance-data.xlsx', sheet_name = 'Scheduled kilometres')
london_underground_operated_km_df = pd.read_excel('./data_source/tfl/operated_km/lu-performance-data.xlsx', sheet_name = 'Operated KMs')

london_underground_operated_km_df
