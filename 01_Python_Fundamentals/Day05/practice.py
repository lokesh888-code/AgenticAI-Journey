# # My Logic
# list1 = []
# studentsCount = int(input("Enter students list count: "))
# for i in range(1,studentsCount+1):
#     print("Enter Student Name",i)
#     name = input("Enter Name ")
#     list1.append(name)

# print("Students List")
# count = 1
# for i in list1:
#     print(count,".",i)
#     count += 1

# AI Logic
students = []
for i in range(5):
    n = input(f"Enter student name {i+1}: ")
    students.append(n)

for i,name in enumerate(students,start=1):
    print(i,".",name)

print(len(students))
