# Exercise 4: Lists
universities = ["ESADE", "MIT", "IE", "IESE", "INSEAD"]

print("List of universities:", universities)
print("First university:", universities[0])
print("Last university:", universities[-1])

# Exercise 5: Dictionaries
student = {
    "name": "John Doe",
    "age": 20,
    "grade": "A"
}

for key, value in student.items():
    print(f"{key}: {value}")