import pandas as pd
#file_name = "convert test5.xlsx"
#file_name = "convert TC.xlsx"
file_name = "toConv.xlsx"

df = pd.read_excel(file_name)
print(df)
df.to_csv("test.csv", index=False, float_format='%.2f')

#pd.read_excel(file_name).to_csv("test.csv", index=False)