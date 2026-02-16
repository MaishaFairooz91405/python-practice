shopping_cart=[]

while True:
    action=input("Add/Remove")
    action=input()
    if action=="Add":
        name=input("Enter the item name: ")
        shopping_cart.append(name)
        print(f"Shopping cart: {shopping_cart}")


    elif action=="Remove":
        name=input("Enter the item name: ")
        if name in shopping_cart:
            shopping_cart.remove(name)
        break
    else:
        print("Invalid action")
# print(f"Shopping cart: {shopping_cart}")
