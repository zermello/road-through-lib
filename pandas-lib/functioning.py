import pandas as pd

# and , or and not of pandas are &, |, and ~

# finding people who are working in finance and there age is greater than 30 and experience greater than 5


data = pd.read_csv("employees_100.csv")

df = pd.DataFrame(data)

page = df[(df["department"] == "Finance") | (df["department"] == "Marketing") & (df["age"] > 10) &(df["experience"] > 5)]
print(page)

page2 = df[df["department"].isin(["Engineering", "Data Science"])]
print(page2)
