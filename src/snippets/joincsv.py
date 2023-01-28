import pandas as pd

df = pd.read_csv('edited_vixarchive.csv')
df2 = pd.read_csv('VIX_History.csv')

finaldf = df.append(df2)

finaldf.to_csv("completed_vix_archive.csv", mode='a', index=False, header=True)