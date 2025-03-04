#Check Even or Odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# Check if a number is positive, negative or zero
num = float(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Age Validation for Drinking
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to Drink.")
else:
    print("You are not eligible to Drink.")

# Find the Largest Number
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    print(f"Largest number is {a}")
elif b >= a and b >= c:
    print(f"Largest number is {b}")
else:
    print(f"Largest number is {c}")

# Check The Leap Year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# Check Divisibility
num = int(input("Enter a number: "))
if num % 5 == 0 and num % 7 == 0:
    print("Divisible by both 5 and 7")
else:
    print("Not divisible by both 5 and 7")

# Grading System
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Check Palidrome

text = input("Enter a word: ")
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

# BMI Calculator
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))
bmi = weight / (height ** 2)
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 24.9:
    print("Normal weight")
elif 25 <= bmi < 29.9:
    print("Overweight")
else:
    print("Obese")

# Check Triangle Type
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))
if a == b == c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")
