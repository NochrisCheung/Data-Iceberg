import pandas as pd
import glob

path  =  './data_source/perth_mint/gold_&_silver_prices/'
all_files = glob.glob(path +'/*.csv')

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

li[3].head(30)
