import pandas as pd

df = pd.read_json("sample_Data.json")  

print('Displying the info of the dataset')
print(df.info())