import pandas as pd

# and , or and not of pandas are &, |, and ~

# finding people who are working in finance and there age is greater than 30 and experience greater than 5


data = pd.read_csv("employees_100.csv")

df = pd.DataFrame(data)
df.iloc[98]

df.isnull()

# for a specified null value dropna for null value
df2 = df.dropna(subset = ["city"])
df2.isnull().sum()

# for every null value
df2 = df.dropna()
df2.isnull().sum()

# or use drop for whole column or anything
df3 = df.drop(columns=["age"])


# how to fill those nun values with specific keywords or values?? -- use .fillna()
df3 = df.fillna("hell")

# or else
df["age"].fillna(df["age"].mean(), inplace=True)
df.isnull().sum()