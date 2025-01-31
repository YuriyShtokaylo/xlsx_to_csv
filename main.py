import pandas as pd
df = pd.read_excel("convert test5.xlsx")
print(df)
df.to_csv("test.csv", index=False, float_format='%.2f')