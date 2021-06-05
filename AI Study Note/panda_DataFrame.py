import pandas as pd
import numpy as np

# Dictionary of list
data = {
    "Name": ["Tom", "Nick", "Krish", "Jack", "Ayuba", "Zsuzsanna", "Monnie"],
    "Age" : [20, 30, 25, 46, np.nan, 23, np.nan],
    "Country": ["Ghana", "Hungary", "Germany", "Nigeria", "USA", "England", " Mali"],
    "Pet":["Dog", "Cat","Crab","Monkey", "Goat", np.nan, np.nan]
}
print(data, "\n")

# Putting Dictionary into pandas into DataFrame
df = pd.DataFrame(data,  index= ["A","B","C","D","E","F","G"])
print(df, "\n")

# Putting DataFrame file into CSV
df_csv =df.to_csv("data.csv")

# Reading CSV file Rows
with open("data.csv", mode="r+") as csv_file:
    for row in csv_file:
        print(row)

#---------------------------------------------------Dealing With Column and Row---------------------------------------
# Column Selections
select_column = df[["Name","Age", "Country"]]
print(select_column, "\n")

# Row Selection
first_row = df.loc["B"]
two_rows = df.loc[["A","C"]]
print(first_row,"\n")
print(two_rows, "\n")

#---------------------------------------------------Working With Missing Data------------------------------------------
# Checking for null or not available
checking_missing_data = df.isnull()
print(checking_missing_data, "\n")

# Filling, replacing or interpolate of not available
filled_Na = df.fillna(0)
print(filled_Na)
""" OR
print(df.replace(np.nan, 0))
"""