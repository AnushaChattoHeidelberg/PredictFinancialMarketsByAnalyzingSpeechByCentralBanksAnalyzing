import pandas as pd
df = pd.read_csv('completed_vix_archive.csv')

for cell in df["DATE"]:
    olddate = str(cell).split('/')
    olddate[0], olddate[1] = olddate[1], olddate[0]
    olddate[0], olddate[2] = olddate[2], olddate[0] 
    newdate = "-".join(olddate)
    df = df.replace({"DATE":cell},{"DATE":newdate})
    #print(newdate)
print(df)
df.to_csv("completed_vix_archive_formatted.csv", mode='a', index=False, header=True)