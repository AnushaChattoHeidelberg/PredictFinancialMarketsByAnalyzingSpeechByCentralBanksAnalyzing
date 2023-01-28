import pandas as pd

df = pd.read_csv('vixarchive.csv')

for cell in df["DATE"]:
    checkstr = str(cell)
    lasttwo = checkstr[-2:]
    if int(lasttwo) >= 90:
        newdate= str(cell[:-2])+'90'+lasttwo
        df = df.replace({"DATE":checkstr},{"DATE":newdate})
    else:
        newdate= str(cell[:-2])+'20'+lasttwo
        df = df.replace({"DATE":checkstr},{"DATE":newdate})
        
print(df)
df.to_csv("edited_vixarchive.csv", mode='a', index=False, header=True)