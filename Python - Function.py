# Exercise 12: Define a Function
def greet(name):
    print(f"Hello, {name}!")

greet("Noor")

# Exercise 13: Function with Return Value
def square(number):
    return number ** 2

print(square(2))
print(square(5))

# Exercise 14: Function with Default Parameters
def multiply(a, b=1):
    return a * b

print(multiply(5, 2))
print(multiply(7))