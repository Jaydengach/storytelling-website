










def calculator():
    # this will be our calculator functions
    # its meant to perform simple arithmetic operations
    owner = "Jayden"
    print("Welcome to "+owner+ "Calculator program")

    print("Select operation")
    print("1 - Addition")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")


    while True:
        # get user input
        choice = input("Enter choice(1/2/3/4)")

        num1 = float(input("Enter the first number"))
        num2 = float(input("enter the second number"))

        if choice == '1':
            print(num1, "+ ", num2, "=", num1+num2)

        elif choice == '2':
            print(num1, "-", num2, "=", num1-num2)

        elif choice == '3':
            print(num1, " *",num2, "=", num1*num2)
        
        elif choice == '4':
            if num2 == 0:
                print("Error: division by zero")
            else:
                print(num1, "/", num2, "=", num1/num2)
        
        break
    else:
        print("invalid input-")
    

calculator()
