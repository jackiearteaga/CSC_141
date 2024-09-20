# Tuple of five basic foods
foods = ("hamburger", "hotdog", "chili", "salad", "pasta")

# Foods in restaurant
print("The restaurant offers the following foods:")
for food in foods:
    print(food)

# Rejected modification
foods[0] = "burrito"

# Changed menu
foods = ("fajita", "dumpling", "chili", "salad", "pasta")

# Print new menu
print("\nThe revised menu:")
for food in foods:
    print(food)