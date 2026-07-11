def addition(a,b):
    return a+b
def subraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    if(b==0):
        return "Division by zero not possible"
    return a+b

print("Enter your choice:")
print("1.Addition")
print("1.Subraction")
print("1.Multiplication")
print("1.Division")

#print("Select Opeartion 1/2/3/4: ")

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter second number : "))
choice  = int(input("Select Opeartion 1/2/3/4: "))

if(choice == 1):
    print("Sum of two numbers",(addition(num1,num2)))
elif(choice == 2):
    print("Sub of two numbers",(subraction(num1,num2)))
elif(choice == 3):
    print("mul of two numbers",(multiplication(num1,num2)))
elif(choice == 4):
    print("Div of two numbers",(division(num1,num2)))
else:
    print("Invalid Choice")