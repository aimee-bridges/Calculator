#Replay calculator function
while True:
    try:
        # User enter numbers
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number entered. Please try again.")
        continue

    # Ask user which operation
    op = input("Enter operation (+, -, *, /): ")

    # Check for addition op
    if op == "+":
        print("Result:", num1 + num2)

    # Check for subtraction op
    elif op == "-":
        print("Result:", num1 - num2)

    # Check for multiplication op
    elif op == "*":
        print("Result:", num1 * num2)

    # Check for division op
    elif op == "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Cannot divide by zero.")

    # If user enters invalid op
    else:
        print("Invalid operation.")

    # Ask user to run calculator again
    repeat = input("Would you like to use the calculator again? (yes/no): ")

    # if user doesn't type yes then loop ends
    if repeat.lower() != "yes":
        break
