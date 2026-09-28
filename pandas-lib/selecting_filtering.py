import numpy as np
import pandas as pd

# selecting and filtering data


data = pd.read_csv("samples/sample.csv")

df = pd.DataFrame(data)
# df = df.set_index("timestamp")


# diff btw loc and iloc
if df.loc[0].all() == df.iloc[0].all():
    print("it works like this")
else:
    print("wrong guess kiddoh!")

# check if both values could be same
if df.loc[0].all() == df.iloc[32].all():
    print("it works like this")
else:
    print("wrong guess kiddoh!") 

df["temperature"] > 25
df[df["temperature"] > 25]

df["timestamp"] == 26.62
df[df["timestamp"] == 26.62]