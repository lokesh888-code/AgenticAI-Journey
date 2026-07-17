students = {
    "name" : "Lokesh",
    "age" : 25,
    "Company" : "Ikyam Solutions"
}

# print(students)

# print(students["name"])
# print(students["age"])

# students["age"] = 24
# print(students)

# del students["Company"]
# print(students)

# students["city"] = "Hydenrabad"
# print(students)

# print(students.get("name"))
# print(students.get("Marks"))
# print(students.get("Marks","Not Found"))

# #Iteration
# for key,value in students.items():
#     print(key,":",value)

# for key in students.keys():
#     print(key)

# for value in students.values():
#     print(value)

for key in students:
    print(key, students[key])