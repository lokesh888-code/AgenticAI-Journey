#My Logic
#items = []
# count = int(input("Enters Items count to add: "))
# for i in range(count):
#     item = input(f"Enter Item {i+1} ")
#     items.append(item)
# removeItem = input("Enter the Item to remove")
# items.remove(removeItem)
# print(items)
# print("Total Items: ",len(items))

# AI logic
items = []
while True:
    print("\n1. Add Item")
    print("2. Remove Item")
    print("3. Display Items")
    print("4. Total Items")
    print("5.Exit")

    choice = int(input("Enter your choice "))
    if(choice == 1):
        item = input("Enter The Item to add in Cart:  ")
        items.append(item)
    elif(choice == 2):
        item = input("Enter the Item to remove from cart: ")
        if item in items:
            items.remove(item)
            print("Item Removed")
        else:
            print(f"The {item} Item is  ot avilable in the cart ")
    elif(choice == 3):
        print("cart = ",items)
    elif(choice == 4):
        print("Total Items in the cart is ",len(items))
    elif(choice == 5):
        break
    else:
        print("Wrong Choice")
    
