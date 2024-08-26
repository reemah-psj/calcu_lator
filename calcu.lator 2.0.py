import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def logarithm(x, base=10):
    try:
        return math.log(x, base)
    except ValueError:
        return "Error! Logarithm undefined for this input."

def exponential(x, y):
    return x ** y

def calculator():
    while True:
        print("\nSelect operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Logarithm")
        print("6. Exponential")
        print("7. Exit")

        # Take input from the user
        choice = input("Enter choice (1/2/3/4/5/6/7): ")

        # Check if the choice is one of the valid options
        if choice in ('1', '2', '3', '4', '5', '6'):
            try:
                if choice in ('5'):  # Logarithm requires only one input
                    num = float(input("Enter number: "))
                    base = input("Enter the logarithm base (default is 10, press Enter to use default): ")
                    if base == '':
                        print(f"The result is: {logarithm(num)}")
                    else:
                        print(f"The result is: {logarithm(num, float(base))}")
                elif choice in ('6'):  # Exponential requires two inputs
                    num1 = float(input("Enter the base number: "))
                    num2 = float(input("Enter the exponent: "))
                    print(f"The result is: {exponential(num1, num2)}")
                else:  # Other operations require two inputs
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))
                    if choice == '1':
                        print(f"The result is: {add(num1, num2)}")
                    elif choice == '2':
                        print(f"The result is: {subtract(num1, num2)}")
                    elif choice == '3':
                        print(f"The result is: {multiply(num1, num2)}")
                    elif choice == '4':
                        print(f"The result is: {divide(num1, num2)}")
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
        elif choice == '7':
            print("Exiting the calculator.")
            break
        else:
            print("Invalid Input")

calculator()
