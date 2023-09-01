import pandas as pd
df = pd.read_excel("Fees.xlsx")
out = {"Name" : [], "Team" : []}
n = 0
for i in df["Fee"]:
    if i == True:
        out["Name"].append(df.iloc[n, 0])
        out["Team"].append(df.iloc[n, 2])
    n += 1
li = []
for name, team in zip(out["Name"], out["Team"]):
    li.append([name, team])
print(li)
df1 = pd.DataFrame(li, columns=["Name", "Committee"], index=range(1, len(li)+1))
print(df1)
df1.to_excel("pack.xlsx")