import pandas as pd
import numpy as np

# lists
a = [1,2,3,4,5,6]

s = pd.Series(a)
print(s)

# dictonaries
b = {
    "akku" : 20,
    "ikku" : 28,
    "kakku" : 19
}

s = pd.Series(b)
print(s)

df = pd.DataFrame([a])
print(df)

# bad dataframe
df = pd.DataFrame([b])
print(df)

# good dataframe
df = pd.DataFrame({
    "name" : ["akku" , "kakku"],
    "age" : [18, 22]
})

print(df)