contact_dict={}
while True:
    print("Choose an option: ")
    print("1. Enter the name and phone number:")
    print("2. Get the contact: ")
    print("3. Delete the contact: ")
    print("4.Print the contact book")

    variable=int(input())
    if variable == 1:
        name=input("Enter your name: ")
        name=name.lower()
        # phone=input("Enter your phone number: ")
        if name in contact_dict.keys():
            print("The name is already in the contact book! Do you want to update the phone number?")
            while True:
                print("1. Yes")
                print("2. No")
                # print("3. Exit")
                choice = input("Enter choice: ")
                if choice == "1":
                    phone=input("Enter your phone number: ")
                    contact_dict[name] = phone
                    break
                elif choice == "2":
                    for name, number in contact_dict.items():
                        print(name, ":", number)
        else:
            phone = input("Enter your phone number: ")
        contact_dict[name]=phone
        print(contact_dict)
        print("Name was added successfully")

# print(contact_dict)
    elif variable == 2:
        name=input("Enter your name: ")
        if name in contact_dict.keys():
            print(contact_dict.get(name))
        else:
            print("Sorry the name not found")

    elif variable == 3:
        name=input("Enter your name: ")
        if name in contact_dict.keys():
            contact_dict.pop(name, "None")
            print(contact_dict)
        else:
            print("Sorry the name not found")
        # contact_dict.pop(name ,"None")
        # print(contact_dict)

    elif variable == 4:
        for name,number in contact_dict.items():
            print(name, ":", number)

    else:
        print("Invalid option")

# print(contact_dict)



