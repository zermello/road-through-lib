import pandas as pd

data = pd.read_csv("employees_100.csv")

df = pd.DataFrame(data)

# filter methods
 
page1 = df[df["department"].isin(["Engineering", "Data Science"])]
print(page1)

page2 = df[df["experience"].between(5, 10)]
print(page2)

page3 = df[df["name"].str.contains("Arjun")]
print(page3)
