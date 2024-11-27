def calculator():
    # Display menu
    print("Simple Calculator")
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Prompt user for input
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose an operation (1/2/3/4 or + / - / * / /): ")

        # Perform the calculation based on user input
        if operation in ['1', '+']:
            result = num1 + num2
            print(f"The result of addition: {num1} + {num2} = {result}")
        elif operation in ['2', '-']:
            result = num1 - num2
            print(f"The result of subtraction: {num1} - {num2} = {result}")
        elif operation in ['3', '*']:
            result = num1 * num2
            print(f"The result of multiplication: {num1} * {num2} = {result}")
        elif operation in ['4', '/']:
            if num2 != 0:
                result = num1 / num2
                print(f"The result of division: {num1} / {num2} = {result}")
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Invalid operation choice. Please choose a valid operation.")
    except ValueError:
        print("Invalid input. Please enter numerical values.")

# Call the function
calculator()
