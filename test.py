import pandas as pandas


data=[
    {"name":"sunny","age":27,"city":"bhopal"},
    {"name":"krish","age":35,"city":"bengaluru"},
    {"name":"sudh","age":33,"city":"delhi"},
]

df=pd.DataFrame(data)

df.to_csv("data/data.csv",index=False)