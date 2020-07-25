usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput  == "admin"  and passwordInput == "1234":
    print("Welcome to Kanomwan shop")
    print("------------------------")
    print("1. chocolate    22.-")
    print("2. browny       17.-")
    print("3. cake         13.-")
    userSelected = int(input("choose >> "))
    if userSelected == 1:
        quantity = int(input("quantity (piece): "))
        cost = 22*quantity
    elif userSelected == 2:
        quantity = int(input("quantity (piece): "))
        cost = 17*quantity
    elif userSelected == 3:
        quantity = int(input("quantity (piece): "))
        cost = 13*quantity
    print("Total cost : ",cost)
    print("--------------------")
    print("Thank you for shopping with us")
else:
    print("username or password is not value")
