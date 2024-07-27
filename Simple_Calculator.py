def calculator():
    print("Select an operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    
    operation = input("Enter operation choice (1/2/3/4): ")
    
    if operation in ['1', '2', '3', '4']:
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))
        
        if operation == '1':
            result = number1 + number2
            print(f"The result of {number1} + {number2} is: {result}")
        elif operation == '2':
            result = number1 - number2
            print(f"The result of {number1} - {number2} is: {result}")
        elif operation == '3':
            result = number1 * number2
            print(f"The result of {number1} * {number2} is: {result}")
        elif operation == '4':
            if number2 != 0:
                result = number1 / number2
                print(f"The result of {number1} / {number2} is: {result}")
            else:
                print("Error! Division by zero.")
    else:
        print("Invalid input. Please select a valid operation.")

# Call the calculator function
calculator()
    
    

