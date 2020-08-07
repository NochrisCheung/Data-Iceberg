import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

fp = './statista/code/statistical-gis-boundaries-london/ESRI/London_Borough_Excluding_MHW.shp'
map_df = gpd.read_file(fp)
map_df
map_df['NAME'].unique()
map_df.plot()
list = ['Westminster']
map_df_selected = map_df
map_df_selected['selected'] = [1 if d in list else 0 for d in map_df['NAME']]
map_df_selected
fig, ax = plt.subplots(1, figsize=(10, 6))

map_df_selected.plot(column='selected', cmap = 'plasma', linewidth=0.8, ax=ax, edgecolor='0.8')
