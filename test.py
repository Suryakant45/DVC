import pandas as pd


data=[
    {"name":"sunny","age":27,"city":"bhopal"},
    {"name":"krish","age":35,"city":"bengaluru"},
    {"name":"sudh","age":33,"city":"delhi"},
    {"name":"vikas","age":29,"city":"up"},
]

df=pd.DataFrame(data)

df.to_csv("data/data.csv",index=False)