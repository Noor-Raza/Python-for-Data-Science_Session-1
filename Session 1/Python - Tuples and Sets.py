# Exercise 6: Tuples
coordinates = (10, 20)

print("Coordinates:", coordinates)
print("X value:", coordinates[0])
print("Y value:", coordinates[1])

# Exercise 7: Sets
colors = {"red", "green", "blue"}
colors.add("yellow")
colors.add("red")  # Adding duplicate, set will ignore it

print("Colors set:", colors)
colors.remove("green")
print("After removing 'green':", colors)

light_colors = {"pink", "white"}
colors.update(light_colors)
print("Merged set:", colors)