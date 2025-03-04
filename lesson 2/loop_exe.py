# Print Numbers from 1 to N
n = int(input("Enter N: "))
for i in range(1, n+1):
    print(i, end=" ")

# Sum of First N Natural Numbers
n = int(input("Enter N: "))
total = sum(range(1, n+1))
print("Sum:", total)

# Print Even Numbers up to N
n = int(input("Enter N: "))
for i in range(2, n+1, 2):
    print(i, end=" ")

# Factorial Of a Number
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial:", fact)

# Multiplication Table
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")

# Count Digits in a Number
num = input("Enter a number: ")
print("Number of digits:", len(num))

# Reverse a Number
num = input("Enter a number: ")
print("Reversed number:", num[::-1])

# Find Sum of Digits
num = input("Enter a number: ")
sum_digits = sum(int(digit) for digit in num)
print("Sum of digits:", sum_digits)

# Check Prime Number
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")

# Star pyrimid
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    print("* " * i)

# Right Align Star Pyramid
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

# Centered Star Pyramid
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)


# Inverted Star Pyrimid
n = int(input("Enter the number of rows: "))
for i in range(n, 0, -1):
    print("* " * i)

# Diamond Star Pattern
n = int(input("Enter the number of rows: "))

# Upper Pyramid
for i in range(1, n + 1, 2):
    print(" " * ((n - i) // 2) + "* " * i)

# Lower Inverted Pyramid
for i in range(n - 2, 0, -2):
    print(" " * ((n - i) // 2) + "* " * i)
