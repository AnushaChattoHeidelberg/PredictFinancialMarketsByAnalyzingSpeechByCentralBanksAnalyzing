#run this code to unzip zipped files in data folder

import zipfile

#add your zip file in the list, please also add the pathname example: data/autoupzippeddata/filename.csv in the gitignore
list_of_files_in_data = ["bis_speeches_tables.zip","merged_finance_1w_2w_split01.zip","merged_finance_1w_2w_split02.zip","merged_finance_1w_2w_split03.zip", "merged_finance_1w_2w_split04.zip", "merged_finance.zip"]

for name in list_of_files_in_data:
    with zipfile.ZipFile("./data/"+name,"r") as zip_ref:
        zip_ref.extractall("./data/autoupzippeddata")