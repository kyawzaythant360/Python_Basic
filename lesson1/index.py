# num1 = float(input("Enter first number: "))  
# num2 = float(input("Enter second number: "))  
# operation = input("Enter operation (+, -, *, /): ")  

# if operation == "+":
#     print("Result:", num1 + num2)
# elif operation == "-":
#     print("Result:", num1 - num2)
# elif operation == "*":
#     print("Result:", num1 * num2)
# elif operation == "/":
#     if num2 != 0:
#         print("Result:", num1 / num2)
#     else:
#         print("Error: Cannot divide by zero")
# else:
#     print("Invalid operation")

# Data Types (String, Integer, Float, Boolean) 


num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))
operation = input("Enter Operation (+, -, *, /): ")


if operation == "+":
    print("Result:", num1 + num2)
elif operation == "-":
    print("Result:", num1 - num2)
elif operation == "*":
    print("Result:", num1 * num2)
elif operation == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:   
        print("Error: Cannot divide by zero")
else:
    print("Invalid Operation")

