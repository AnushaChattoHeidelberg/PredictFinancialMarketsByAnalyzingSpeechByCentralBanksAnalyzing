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
    "Diff_VIX_2w": [],
    "date1w": [],
    "date2w": []
}

'''

date1_2w = {
    "date1w": [],
    
    "date2w": []
    
}
'''

#df_market["Diff_VIX_1w"] = np.nan

stored_df = pd.DataFrame(data)
#df1_2w = pd.DataFrame(date1_2w)


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



print("oneweeklist and twoweek created")


print(stored_df.head(5))

#stored_df['Diff_VIX_1w'] = stored_df['OPEN'].where(stored_df['date1w'] == stored_df['DATE'])
one_w = timedelta(weeks = 1)
two_w = timedelta(weeks = 2)
stored_df['DATE'] = pd.to_datetime(stored_df['DATE'])
stored_df['date1w'] = stored_df['DATE'] + one_w
stored_df['date2w'] = stored_df['DATE'] + two_w
#stored_df['date1w'] = pd.to_datetime(stored_df['date1w'])
#stored_df['date2w'] = pd.to_datetime(stored_df['date2w'])
stored_df = stored_df.sort_values(by='DATE')
size = len(stored_df.index)
w1_rows = 0
w2_rows = 0
print(stored_df.tail(5))
finaldf=pd.DataFrame(data)
i=0
for index, row in stored_df.iterrows():
        os.system('clear')
        print('processing row',i,'outof',size)
        #this logic is inefficient but I am too lazy to fix it, due to repeating articles
        #print('number of rows with 1w',w1_rows)
        #print('number of rows with 2w',w2_rows)
        #print(finaldf.head(5))
        #check = datetime.now()
        for index2, row2 in stored_df.iterrows():
            if row2['DATE'] == row['date1w']:
               # if(row2['DATE'] == check):
                #    pass
                #else:
                row['Diff_VIX_1w'] = row2['OPEN']
                    #check = row['Diff_VIX_1w']
                w1_rows += 1
             #  check = row2['DATE']
                #print(row)
                #print("1w matched")
            
            if row2['DATE'] == row['date2w']:
                row['Diff_VIX_2w'] = row2['OPEN']
                #print("2w matched")
                w2_rows += 1
                break
        finaldf = finaldf.append(row)
        i += 1

print('table completed')


'''
now = datetime.now()

date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

date= str(date_time)
'''

#print(stored_df.head(5))
finaldf.to_csv("merged_finance_1w_2w"+".csv", mode='a', index=False, header=True)

