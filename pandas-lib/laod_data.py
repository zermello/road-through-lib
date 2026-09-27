import pandas as pd
import numpy as np

data = pd.read_csv("samples/sample.csv")

df = pd.DataFrame(data)
print(df)

test = df["timestamp"][0:10]

print(df.describe())
print(df.head(10))
print(df.tail(5))
print(df.shape)
print(df.keys())
print(df.sample())
print(df.dtypes)
print(df.info())

data = pd.read_xml("samples/sample.xml",
                    parser="etree",
                    xpath=".//sensor",
                    )

df = pd.DataFrame(data)
print(df)

data = pd.read_json("samples/sample.json")

df = pd.DataFrame(data)
print(df)