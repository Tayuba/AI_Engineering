import numpy as np
# 1. Import pandas under the name pd
import pandas as pd

# 2. Print the version of pandas that has been imported.
print(pd.__version__)

# 3. Print out all the version information of the libraries that are required by the pandas library.
print(pd.show_versions())

# 4. Create a DataFrame df from this dictionary data which has the index labels.
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(data, index=labels)

# 5. Display a summary of the basic information about this DataFrame and its data
print(df)
print("\n")

# 6. Return the first 3 rows of the DataFrame df
row_3 = df.loc["a":"c"]
print(row_3)
print("\n")

# 7. Select just the 'animal' and 'age' columns from the DataFrame df
column_2 = (df[["animal", "age"]])
print(column_2)
print("\n")

# 8. Select the data in rows [3, 4, 8] and in columns ['animal', 'age'].
row_3_4_8 = column_2.loc[list("cdh")]
print(row_3_4_8)
print("\n")

# 9. Select only the rows where the number of visits is greater than 2
row_greaterthan_2 = df.loc[df.visits > 2]
print(row_greaterthan_2)
print("\n")

# 10. Select the rows where the age is missing, i.e. is NaN
missing_values = df[df.isna().any(axis=1)]
print(missing_values)
print("\n")

# 11. Select the rows where the animal is a cat and the age is less than 3.
cat_age_less_3 = df[(df["animal"] == "cat") & (df["age"] < 3)]
print(cat_age_less_3)
print("\n")

# 12. Select the rows the age is between 2 and 4 (inclusive)
age_bet_2_4 = df[df["age"].between(2, 4)]
print(age_bet_2_4)
print("\n")

# 13. Change the age in row 'f' to 1.5
change_age = df.loc["f", "age"] = 1.5
print(df)
print("\n")

# 14. Calculate the sum of all visits (the total number of visits)
sum_of_visit = df["visits"].sum()
print(sum_of_visit)
print("\n")

# 15. Calculate the mean age for each different animal in df.
print(df)
mean_of_age = df.groupby("animal")["age"].mean()
print(mean_of_age)
print("\n")

# 16. Append a new row 'k' to df with your choice of values for each column. Then delete that row to return the original DataFrame.
added_row = df.loc["k"] = ["crab", 17.45, 24, 19]
print(f"Added row \n{df}")
deleted_row = df = df.drop("k")
print("\n")
print(f"deleted row \n {deleted_row}\n")

# 17. Count the number of each type of animal in df
count_animals = df['animal'].value_counts()
print(count_animals,"\n")

# 18. Sort df first by the values in the 'age' in decending order, then by the value in the 'visit' column in ascending order.
sorting_by_order = df.sort_values(by=["age", "visits"], ascending=[False, True])
print(sorting_by_order, "\n")

# 19. The 'priority' column contains the values 'yes' and 'no'. Replace this column with a column of boolean values: 'yes' should be True and 'no' should be False
Bool_yes_no = df["priority"].map({"yes": True, "no": False})
print(Bool_yes_no, "\n")

# 20. In the 'animal' column, change the 'snake' entries to 'python'.
replace_animal = df["animal"].replace("snake", "python")
print(replace_animal, "\n")

# 21. For each animal type and each number of visits, find the mean age. In other words, each row is an animal, each column is a number of visits and the values are the mean ages (hint: use a pivot table)
special_mean = df.pivot_table(index="animal", columns="visits", values="age", aggfunc="mean")
print(special_mean, "\n")

# 22. You have a DataFrame df with a column 'A' of integers. For example:
# How do you filter out rows which contain the same integer as the row immediately above?
df = pd.DataFrame({"A": [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7]})
inter_same = df.loc[df["A"].shift() != df["A"]]
print(inter_same, "\n")

# 23 Given a DataFrame of numeric values, say
df = pd.DataFrame(np.random.random(size=(5, 3))) # a 5x3 frame of float values
# how do you subtract the row mean from each element in the row?
row_mean_sub = df.sub(df.mean(axis=1), axis=0)
print(row_mean_sub, "\n")

# 24. Suppose you have DataFrame with 10 columns of real numbers, for example:
df = pd.DataFrame(np.random.random(size=(5, 10)), columns=list("abcdefghij"))
# Which column of numbers has the smallest sum? (Find that column's label.

smallest_sum = df.sum().idxmin()
print(smallest_sum, "\n")

# 25. How do you count how many unique rows a DataFrame has (i.e. ignore all rows that are duplicates)?
duplica_values = len(df.drop_duplicates(keep=False))
print(duplica_values, "\n")

# 26. You have a DataFrame that consists of 10 columns of floating--point numbers. Suppose that exactly 5 entries in each row are NaN values. For each row of the DataFrame, find the column which contains the third NaN value.
# (You should return a Series of column labels. Try not to use .iterrows())
data = {
1:[np.nan,2,np.nan,4,5],
2:[np.nan,2,3,np.nan,5],
3:[np.nan,2,np.nan,4,5],
4:[1,np.nan,3,np.nan,np.nan],
5:[1,2,np.nan,4,5],
6:[1,np.nan,3,np.nan,np.nan],
7:[1,2,3,4,5],
8:[1,np.nan,3,np.nan,np.nan],
9:[1,2,3,4,np.nan],
10:[1,np.nan,3,4,5]}
pos_3_NaN = (df.isnull().cumsum(axis=1) == 3).idxmax(axis=1)
print(pos_3_NaN, "\n")

# 27. A DataFrame has a column of groups 'grps' and and column of numbers 'vals'. For example:
df = pd.DataFrame({"grps": list("aaabbcaabcccbbc"),
                   "vals": [12,345,3,1,45,14,4,52,54,23,235,21,57,3,87]})
# For each group, find the sum of the three greatest values.

sum_grp_3 = df.groupby("grps")["vals"].nlargest(3).sum(level=0)
print(sum_grp_3)