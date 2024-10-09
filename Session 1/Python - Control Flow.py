# Exercise 8: Conditional Statements
num = float(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# Exercise 9: For Loop
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)

# Exercise 10: While Loop
counter = 1

while counter <= 5:
    print(counter)
    counter += 1

# Exercise 11: Match Statement
grade = input("Enter your grade (A, B, C, D, F): ")

match grade:
    case "A":
        print("Excellent!")
    case "B":
        print("Good job!")
    case "C":
        print("Fair.")
    case "D":
        print("Needs improvement.")
    case "F":
        print("Failing.")
    case _:
        print("Invalid grade.")