# Empty list to store toppings
toppings = []

# Loop to get pizza toppings
while True:
    topping = input("Enter a pizza topping (or type 'quit to finish): ")
    # Check if user want to quit
    if topping.lower() == 'quit':
        break

    # Add the topping to the list and print message
    toppings.append(topping)
    print("I'll add " + topping + " to your pizza.")

# All the toppings added
print("\nYour pizza will have the following toppings:")
for topping in toppings:
    print(topping)