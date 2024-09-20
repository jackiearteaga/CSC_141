# 4_11 Exercise
#  My list
fav_Pizzas = ["cheese", "alfredo", "sicilian"]

# Copy of list for friend
friends_Pizzas = fav_Pizzas.copy()

# New pizza
fav_Pizzas.append("hawaiian")

# Diff pizza for friend
friends_Pizzas.append("margherita")

# Show two separate lists
print("My favorite pizzas are:")
for pizza in fav_Pizzas:
                print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friends_Pizzas:
                print(pizza)

# 4_12 Exercise
# List fruits
fruits = ["strawberry", "pomegranate", "mango", "grape"]

# List veggies
veggies = ["avocado", "tomato", "onion", "asparagus"]

# For loop fruits
print("My fav fruits are:")
for fruit in fruits:
                print(fruit)

# For loop veggies
print("\nMy fav veggies are:")
for veg in veggies:
                print(veg)

# 4_13 Exercise
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