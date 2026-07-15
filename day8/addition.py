def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def  main():
    print("This is a simple calculator module. You can use the add, subtract, multiply, and divide functions.")
    print("Select a choice:")
    print("1. Addition")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = int(input("Enter your choice (1-4): "))
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if choice == 1:
        print(f"The result of addition is: {add(num1, num2)}")
    elif choice == 2:
        print(f"The result of subtraction is: {subtract(num1, num2)}")
    elif choice == 3:
        print(f"The result of multiplication is: {multiply(num1, num2)}")
    elif choice == 4:
        try:
            result = divide(num1, num2)
            print(f"The result of division is: {result}")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()