

inventory = {}

while True:
    print("1. Add Item")
    print("2. Update Item")
    print("3. Delete Item")
    print("4. View Inventory")
    print("5. Exit")

    choice = input("Enter choice: ")


    if choice == "1":
        name = input("Item name: ")
        # qty = int(input("Quantity: "))
        if name in inventory.keys():
            print("The item is already in the inventory! Do you want to update the quantity?")
            while True:
                print("1. Yes")
                print("2. No")
                # print("3. Exit")
                choice = input("Enter choice: ")
                if choice == "1":
                    qty = int(input("Quantity: "))
                    inventory[name] = qty
                    break
                elif choice == "2":
                    print("Inventory List:")
                    for item, qty in inventory.items():
                        print(item, ":", qty)

        else:
            qty = int(input("Quantity: "))
        inventory[name] = qty
        print("Item added successfully!")



    elif choice == "2":
        name = input("Item name: ")

        if name in inventory.keys():
            qty = int(input("New quantity: "))
            inventory[name] = qty
            print("Item updated!")
        else:
            print("Item not found!")



    elif choice == "3":
        name = input("Item name: ")

        if name in inventory.keys():
            del inventory[name]
            print("Item deleted!")
        else:
            print("Item not found!")



    elif choice == "4":
        print("Inventory List:")
        for item, qty in inventory.items():
            print(item, ":", qty)



    else:
        print("Invalid choice")
