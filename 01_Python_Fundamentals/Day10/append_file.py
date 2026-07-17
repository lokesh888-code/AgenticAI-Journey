with open("students.txt","r") as file:
    print(file.read())

with open("students.txt","a") as file:
    file.write("\n Mango")

with open("students.txt","r") as file:
    print(file.read())

file.close