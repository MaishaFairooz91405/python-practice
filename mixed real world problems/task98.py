
expense_tracker={}

while True:
    print("1. Add Item")
    print("2. Update Item")
    print("3. Delete Item")
    print("4. View Inventory")
    print("5. Calculate the total cost")
    print("6. Exit")

    choice = input("Enter choice: ")


    if choice == "1":
        name = input("Item name: ")

        if name in expense_tracker.keys():
            print("The item is already in the expense tracker! Do you want to update the cost?")
            while True:
                print("1. Yes")
                print("2. No")

                choice = input("Enter choice: ")
                if choice == "1":
                   cost= int(input("enter the cost: "))
                   expense_tracker[name] = cost
                   break
                elif choice == "2":
                    print("Expense Tracker:")
                    for item,cost in expense_tracker.items():
                        print(item, ":", cost)

        else:
            cost= int(input("enter the cost: "))
        expense_tracker[name] = cost
        print("Item added successfully!")



    elif choice == "2":
        name = input("Item name: ")

        if name in expense_tracker.keys():
           cost= int(input("enter the cost: "))
           expense_tracker[name] = cost
           print("Item updated!")
        else:
            print("Item not found!")



    elif choice == "3":
        name = input("Item name: ")

        if name in expense_tracker.keys():
            del expense_tracker[name]
            print("Item deleted!")
        else:
            print("Item not found!")



    elif choice == "4":
        print("Inventory List:")
        for item, cost in expense_tracker.items():
            print(item, ":", cost)

    elif choice == "5":
        for cost in expense_tracker.values():
            print(sum(cost))
    else:
        print("Invalid choice")
