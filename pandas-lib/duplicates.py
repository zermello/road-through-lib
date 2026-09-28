import pandas as pd


data = pd.read_csv("employees_100.csv")
df = pd.DataFrame(data)

#finding duplicate
df.duplicated(subset=["employee_id"]).sum()

# dropping duplicate
df3  = df.drop_duplicates(subset=["employee_id"])
df3.duplicated(subset=["employee_id"]).sum()

# to have normal indexing and remove setted index

df.set_index("employee_id")
df.reset_index()

# balance portion