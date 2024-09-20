# List comprehension
cubes = [number**3 for number in range(1, 11)]

# List of cubes
print("The list of cubes:", cubes)

# First three items
print("\nThe first three items in the list are:", cubes[:3])

# Three items from middle
middle = len(cubes) // 2
print("\nThree items from the middle of the list are:", cubes[middle - 1:middle + 2])

# Last three items
print("\nThe last three items in the list are:", cubes[-3:])