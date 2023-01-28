import os
import pandas as pd
import numpy as np
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
'''

for date in stored_df["DATE"]:
    date_list = str(date).split('-')
    date_list = list(map(int, date_list))
    print(date_list)
    one_week_date = date_list.copy()
    two_week_date = date_list.copy()
    if (date_list[1] == 2):
        if (date_list[0] % 4 == 0 and date_list[0] % 100 != 4):
            if (date_list[2] < 23):
                    if(date_list[2] < 16):
                        one_week_date[2] = date_list[2]+7
                        two_week_date[2] = date_list[2]+14
                    else:
                        one_week_date[2] = date_list[2]+7
                        temp = date_list[2]+14
                        temp = temp-29
                        two_week_date[2] = temp
                
                        two_week_date[1] = date_list[1] + 1
                        
            else:
                    temp = date_list[2]+7
                    temp = temp-29
                    temp2 = date_list[2]+14
                    temp2 = temp2-29
                    one_week_date[2] = temp
                    two_week_date[2] = temp2

                    one_week_date[1] = date_list[1] + 1
                    two_week_date[1] = date_list[1] + 1

                
        else:
                if (date_list[2] < 22):
                    one_week_date[2] = date_list[2]+7
                    if(date_list[2] < 15):
                        one_week_date[2] = date_list[2]+7
                        two_week_date[2] = date_list[2]+14
                    else:
                        one_week_date[2] = date_list[2]+7
                        temp = date_list[2]+14
                        temp = temp-28
                        two_week_date[2] = temp

                        two_week_date[1] = date_list[1] + 1

                else:
                    temp = date_list[2]+7
                    temp = temp-29
                    temp2 = date_list[2]+14
                    temp2 = temp2-29
                    one_week_date[2] = temp
                    two_week_date[2] = temp2
     
                    one_week_date[1] = date_list[1] + 1
                    two_week_date[1] = date_list[1] + 1
                 
    elif (date_list[1] == 4 or date_list[1] == 6 or date_list[1] == 9 or date_list[1] == 11):
        if (date_list[2] < 24):
            if(date_list[2] < 17):
                        one_week_date[2] = date_list[2]+7
                        two_week_date[2] = date_list[2]+14
            else:
                        one_week_date[2] = date_list[2]+7
                        temp = date_list[2]+14
                        temp = temp-30
                        two_week_date[2] = temp
                           
                        two_week_date[1] = date_list[1] + 1
                    
        else:
                    temp = date_list[2]+7
                    temp = temp-30
                    temp2 = date_list[2]+14
                    temp2 = temp2-30
                    one_week_date[2] = temp
                    two_week_date[2] = temp2
                    
                    one_week_date[1] = date_list[1] + 1
                    two_week_date[1] = date_list[1] + 1
                    
    elif (date_list[1] == 1 or date_list[1] == 3 or date_list[1] == 5 or date_list[1] == 7 or date_list[1] == 8 or date_list[1] == 10 or date_list == 12):
        if (date_list[2] < 25):
            if(date_list[2] < 18):
                        one_week_date[2] = date_list[2]+7
                        two_week_date[2] = date_list[2]+14
            else:
                        one_week_date[2] = date_list[2]+7
                        temp = date_list[2]+14
                        temp = temp-31
                        two_week_date[2] = temp
                        if (date_list[1] != 12):
                            
                            two_week_date[1] = date_list[1] + 1
                        else:
                            two_week_date[1] = 1
                            two_week_date[0] = date_list[0] + 1
        else:
                    temp = date_list[2]+7
                    temp = temp-31
                    temp2 = date_list[2]+14
                    temp2 = temp2-31
                    one_week_date[2] = temp
                    two_week_date[2] = temp2
                    if (date_list[1] != 12):
                        one_week_date[1] = date_list[1] + 1
                        two_week_date[1] = date_list[1] + 1
                    else:
                        one_week_date[1] = 1
                        one_week_date[0] = date_list[0] + 1
                        two_week_date[1] = 1
                        two_week_date[0] = date_list[0] + 1
   

    one_week_date_join = str(
        one_week_date[0]) +'-'+ str(one_week_date[1]) +'-'+ str(one_week_date[2])
    print(one_week_date)

    two_week_date_join = str(
        two_week_date[0]) +'-'+ str(two_week_date[1]) +'-'+ str(two_week_date[2])
    print(two_week_date)

    one_two_week_date_join_df = {
        "date1w" : one_week_date_join,
        "date2w" : two_week_date_join
    }
    df1_2w= df1_2w.append(one_two_week_date_join_df, ignore_index = True)




print("oneweeklist and twoweek created")
#placeholder = date1_2w.copy()
df_market = df_market.rename(columns={"DATE":"date1w","CLOSE":"Diff_VIX_1w"})
#df1_2w = df1_2w.fillna(df1_2w[["CLOSE"]].merge(df_market, on="DATE", how='left'))
#df1_2w.update(df1_2w[['DATE', 'CLOSE']].merge(df_market, 'left'))
#df1_2w = df1_2w.update(df_market)
#df1_2w['Diff_VIX_1w'] = df_market['CLOSE']
#df1_2w = df1_2w.join(df_market, on="DATE")
#df1_2w["Diff_VIX_1w"] = df_market.where(df1_2w["DATE"] == df_market["DATE"])
df1_2w = df1_2w.merge(df_market, on='date1w')
#print(df1_2w)
'''

'''
for index in df1_2w.index:
    stored_df.at[index,'Diff_VIX_1w'] = stored_df.query("DATE=='" + df1_2w.at[index,'date1w'] + "'" )["OPEN"]
    stored_df.at[index,'Diff_VIX_2w'] = stored_df.query("DATE=='" + df1_2w.at[index,'date2w'] + "'" )["OPEN"]
'''

print(stored_df.head(5))
stored_df.to_csv("merged_finance.csv", mode='a', index=False, header=True)

