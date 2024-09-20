# My list
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