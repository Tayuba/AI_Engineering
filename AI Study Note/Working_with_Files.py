#---------------------------------------------- Two was of opening Files--------------------------------------------

# Opening file in the same directory location as python file
file_in_same_dir = open("C:/Users/Zsazs/OneDrive/Dokumentumok/GitHub/AI_Engineering/AI Study Note/study.txt", mode="r")

# Opening file with different file location as python file
file_in_diff_dir = open("C:/Users/Zsazs/PycharmProjects/pythonProject1/pythonProject/Reading_Writing_File/my_file.txt", mode="r")


#------------------------------------------------ Closing file, there are two method------------------------------------

# Method one(1) for closing files
file_in_same_dir.close()
file_in_diff_dir.close()

# Method two(2) for closing files
with open("C:/Users/Zsazs/OneDrive/Dokumentumok/GitHub/AI_Engineering/AI Study Note/study.txt", mode="r") as file_in_same_dir:
    print(file_in_same_dir.read())
with open("C:/Users/Zsazs/PycharmProjects/pythonProject1/pythonProject/Reading_Writing_File/my_file.txt", mode="r") as file_in_diff_dir:
    print(file_in_diff_dir.read())

#-----------------------------------------------Writing into File----------------------------------------------------------

# There are two ways of writing into a single text file

# Method one(1), allows only single string to be inserted into a single file.
str_1 = "My name is Ayuba\n"
str_2 = "I am from Ghana\n"
str_3 = "I live in Kaiserslautern"
Multi_Str = [str_1, str_2, str_3]

with open("study.txt", mode="w+") as file_in_same_dir:
    file_in_same_dir.write(str_1)

# Method two(2) , inserting multiple strings in a single text file
with open("study.txt", mode="w+") as file_in_same_dir:
    file_in_same_dir.writelines(Multi_Str)


#----------------------Reading File, Writing, Appending with all the various read and access modes---------------------

text1 = ["My name is Ayuba\n", "I am from Ghana\n", "I live in Kaiserslautern"]
# Creating file and opening
with open("Ayuba.txt", mode="w") as text:
    print(text.writelines(text1))

#
import pandas as pd
df = pd.DataFrame({"Data1": [10, 20, 30], "Date2": [40, 50, 60]})
norm_df = ((df-df.min()) / (df.max()-df.min()))
print(norm_df)
