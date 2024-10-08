# Empty list to store the toppings
toppings = []
active = True  # Active variable to control loop

# Conditional test in the while statement
while active:
    topping = input("Enter a pizza topping (or type 'quit' to finish): ")

    # Use break statement to exit the loop
    if topping.lower() == 'quit':
        break  # Exits the loop

    # Add the topping to the list and print message
    toppings.append(topping)
    print("I'll add " + topping + " to your pizza.")

# Print all toppings added
print("\nYour pizza will have the following toppings:")
for topping in toppings:
    print(topping)
