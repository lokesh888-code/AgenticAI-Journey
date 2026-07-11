items = []

def add_items():
    while True:
        item = input("Enter item to add (type done to stop): ")
        if item.lower() == "done":
            break
        items.append(item)
        print(item, "added")

def remove_item():
    item = input("Enter item to remove: ")
    if item in items:
        items.remove(item)
        print(item, "removed")
    else:
        print(item, "not found")

def display_cart():
    print("Cart:", items)

def total_items():
    print("Total Items:", len(items))

while True:
    print("\n1. Add Item")
    print("2. Remove Item")
    print("3. Display Cart")
    print("4. Total Items")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_items()
    elif choice == "2":
        remove_item()
    elif choice == "3":
        display_cart()
    elif choice == "4":
        total_items()
    elif choice == "5":
        break
    else:
        print("Invalid choice")