# List of cities
cities = ["New York", "San Francisco", "Chicago", "Boston", "Atlanta"]

# Original list
print("Original list: ")
print(cities)

# Number of cities
print("\nNumber of cities:", len(cities))

# Adding new city
cities.append("Pheonix")
print("\nList after appending city: ")
print(cities)

# Inserting another city
cities.insert(0, "Philadelphia")
print("\nList after inserting new city: ")
print(cities)

# Remove a city
cities.remove("San Francisco")
print("\nList after removing city:")
print(cities)

# Remove using pop
removed_City = cities.pop()
print("\nRemoved city:", removed_City)
print("List after using pop():")
print(cities)

# Alphabetical order using sort()
cities.sort()
print("\nList sorted in alphabetical with sort():")
print(cities)

# Reverse order of cities
cities.reverse()
print("\nList reversed:")
print(cities)

# Print in alphabetical without modifying list
print("\nList in alphabetical:")
print(sorted(cities))

# Still in reversed order
print("\nOriginal list after sorted:")
print(cities)

# Reverse and restore order
cities.reverse()
print("\nList reversed to original:")
print(cities)