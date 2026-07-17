# import os
# os.chdir(r"D:\D Drive\PythonDay10")
# print(os.getcwd())

with open("students.txt","r") as file:
    data = file.read()

print(data)