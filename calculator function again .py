
def main():
    print("type here")
    num1 = int(input("Enter the first number: "))
    operation = input("Enter the operation (+, -, *, /): ")
    num2 = int(input("Enter the second number: "))

    if operation == '+':
        print("Result: ", (num1 + num2))
    elif operation == '-':
        print("Result: ", (num1 - num2))
    elif operation == '*':
        print("Result: ", (num1 * num2))
    elif operation == '/':
        print("Result: ", (num1 / num2))
    else:
        print("Oops! Invalid operation. Please try again!")
main()