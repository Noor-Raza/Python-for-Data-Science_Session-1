# Exercise 15: List Comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [number ** 2 for number in numbers]

print(squares)

# Exercise 16: Nested Data Structures
students_grades = {
    "Alice": [90, 85, 88],
    "Bob": [75, 80, 82],
    "Charlie": [95, 92, 93]
}

def calculate_average(grades):
    return sum(grades) / len(grades)

for student, grades in students_grades.items():
    print(f"{student}'s average grade is: {calculate_average(grades):.2f}")

# Exercise 17: Simple Calculator
def calculate(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    else:
        return "Invalid operator"

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

result = calculate(num1, num2, operator)
print(f"Result: {result}")
