import pandas as pd

df = pd.read_csv("Sales_data_sample.csv",encoding="utf-8")

print(df.describe())