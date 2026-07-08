#enumerator is used to get index while printing list. It starts with 0
#So we use srart parameter to indicate where to start.
names = ["A","B","C","D"]
for name in names:
    print(name)
print()
for i,name in enumerate(names,start = 1):
    print(i,name)