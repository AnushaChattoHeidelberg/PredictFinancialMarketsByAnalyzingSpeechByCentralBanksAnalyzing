import os
import pandas as pd

#location_str = "bank indonesia"

directory = "./BIS_speeches_2021_03_03/2_scraped_2021_03_03_txt/"


data = {
    "date": [],
    "article": [],
}

storeddf = pd.DataFrame(data)
#storeddf.to_csv(x[0]+'.csv')
for x in os.walk(directory):
    for name in x[1]:
        storeddf.to_csv(x[0]+'.csv')
        for filename in os.listdir("./BIS_speeches_2021_03_03/2_scraped_2021_03_03_txt/"+name + '/'):
            if filename.endswith(".txt"): 
                with open("./BIS_speeches_2021_03_03/2_scraped_2021_03_03_txt/"+name + '/' + filename) as f:
                    contents = f.readlines()
                date_1 = filename[:-6]
                data2 = {
                    "date": [date_1],
                    "article": [contents]
                }
                storeddf = pd.DataFrame(data2)
                csvfilename= name+'.csv'
                storeddf.to_csv(csvfilename, mode='a', index=False, header=False)

                # print(os.path.join(directory, filename))
                continue
            else:
                continue