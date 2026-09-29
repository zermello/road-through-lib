import pandas as pd

data = pd.read_csv("employees_100.csv")
df = pd.DataFrame(data)

df["department"].rename("section")