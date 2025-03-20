# 1. Greet a User
def greet_user(name):
    print(f"Hello, {name}! Welcome to Python.")

greet_user("Alice")  # Output: Hello, Alice! Welcome to Python.

# 2. Find the Maximum of Two Numbers
def find_max(a, b):
    return a if a > b else b

print(find_max(10, 25))  # Output: 25

# 3. Check if a Number is Even
def is_even(n):
    return n % 2 == 0

print(is_even(4))  # Output: True
print(is_even(7))  # Output: False

# 4. Calculate the Factorial of a Number
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

print(factorial(5))  # Output: 120

# 5. Count Vowels in a String
def count_vowels(s):
    return sum(1 for char in s.lower() if char in "aeiou")

print(count_vowels("Hello World"))  # Output: 3

# 6. Reverse a String
def reverse_string(s):
    return s[::-1]

print(reverse_string("Python"))  # Output: nohtyP

# 7. Check if a Number is Prime
def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

print(is_prime(7))  # Output: True
print(is_prime(10)) # Output: False
