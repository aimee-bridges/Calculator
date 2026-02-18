#User enter numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


#Ask user which operation
op = input("Enter operation (+, -, *, /): ")

#Check for addition op
if op == "+":
    print("Result:", num1 + num2)

#Check for subtraction op
elif op == "-":
    print("Result:", num1 - num2)

#Check for multiplication op
elif op == "*":
    print("Result:", num1 * num2)

#Check for division op
elif op == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Cannot divide by zero.")

#If user enters invalid op
else:
    print("Invalid operation.")