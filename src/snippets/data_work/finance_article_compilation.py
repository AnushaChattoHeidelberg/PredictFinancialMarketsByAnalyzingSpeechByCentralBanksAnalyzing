import os
import pandas as pd
import numpy as np
from datetime import datetime
from datetime import timedelta
df_market = pd.read_csv('completed_vix_archive_formatted.csv')
directory = "./bis_speeches_tables_2/"
data = {
    "DATE": [],
    "ARTICLE": [],
    "Diff_VIX_1d": [],
    "Diff_VIX_1w": [],
    "Diff_VIX_2w": []
}



date1_2w = {
    "date1w": [],
    
    "date2w": []
    
}

#df_market["Diff_VIX_1w"] = np.nan

stored_df = pd.DataFrame(data)
df1_2w = pd.DataFrame(date1_2w)


for filename in os.listdir(directory):
    df_file = pd.read_csv(directory + filename)
    mergedDF = pd.merge(df_file, df_market, on=['DATE'], how='inner')
    # print(df_file.columns)
    # if(df_market['DATE'].isin(df_file['DATE']).value_counts()):
    #   print("true")
    stored_df = stored_df.append(mergedDF)
    #print("merged")
stored_df["Diff_VIX_1d"] = stored_df["CLOSE"]
#print("1d values added")
    # df_1w = np.where(stored_df['DATE'] == (df_market['DATE']))


for date in stored_df["DATE"]:
    date_list = str(date).split('-')
    date_list = list(map(int, date_list))
    print(date_list)
    one_w = timedelta(weeks = 1)
    two_w = timedelta(weeks = 2)
    #one_week_date = date_list.copy()
    #two_week_date = date_list.copy()
    current_date_obj = datetime(date_list[0], date_list[1], date_list[2], 00, 00)
    one_week_obj = current_date_obj + one_w
    two_week_obj = current_date_obj + two_w
    one_week_date = [one_week_obj.year, one_week_obj.month , one_week_obj.day]
    print(one_week_date)
    date1= "-".join(str(x) for x in one_week_date)
    two_week_date = [two_week_obj.year, two_week_obj.month , two_week_obj.day]
    print(two_week_date)
    date2="-".join(str(x) for x in two_week_date)
    
    tempdf_date = {
    "date1w": [date1],
    
    "date2w": [date2]
    
    }
    tempdf = pd.DataFrame(tempdf_date)
    df1_2w = df1_2w.append(tempdf)


df1_2w = df1_2w.reset_index(drop=True)

print("oneweeklist and twoweek created")
#placeholder = date1_2w.copy()
#df_market = df_market.rename(columns={"DATE":"date1w","CLOSE":"Diff_VIX_1w"})
#df1_2w = df1_2w.fillna(df1_2w[["CLOSE"]].merge(df_market, on="DATE", how='left'))
#df1_2w.update(df1_2w[['DATE', 'CLOSE']].merge(df_market, 'left'))
#df1_2w = df1_2w.update(df_market)
#df1_2w['Diff_VIX_1w'] = df_market['CLOSE']
#df1_2w = df1_2w.join(df_market, on="DATE")
#df1_2w["Diff_VIX_1w"] = df_market.where(df1_2w["DATE"] == df_market["DATE"])
#df1_2w = df1_2w.merge(df_market, on='date1w')
#print(df1_2w.head(5))

print(df1_2w.head(5))
print(stored_df.head(5))

for index in df1_2w.index:
 
    #print(str(df1_2w.at[1,'date2w']))
    ex1= "DATE=='" + str(df1_2w.at[index,'date1w']) + "'"
    ex2 = "DATE=='" + str(df1_2w.at[index,'date2w']) + "'" 
    stored_df.at[index,'Diff_VIX_1w'] = stored_df.eval(ex1 )['OPEN']
    stored_df.at[index,'Diff_VIX_2w'] = stored_df.eval(ex2 )['OPEN']



'''
now = datetime.now()

date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
'''
print(stored_df.head(5))
#stored_df.to_csv("merged_finance"+date_time+".csv", mode='a', index=False, header=True)

