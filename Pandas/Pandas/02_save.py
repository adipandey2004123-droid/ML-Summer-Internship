import pandas as pd

data = {

    "Name":['Ram','Adi','Vedanti','Sitanshu'],
    "Age":[10,22,21,21],
    "City":['Nagpur','Mumbai','Delhi','Lucknow']
}

df = pd.DataFrame(data)
# print(df)  
# df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx", index=False)
df.to_json("output.json", index=False)