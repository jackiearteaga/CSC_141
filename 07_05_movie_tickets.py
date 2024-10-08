# Loop to ask for the user's age
while True:
    age = input("Please enter your age (or type 'quit' to exit): ")

    # Check if they want to quit
    if age.lower() == 'quit':
        break

    # Convert the input to an integer
    age = int(age)

    # Determine the ticket price based on age
    if age < 3:
        price = "free"
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15

    # Print the ticket price
    print("The ticket price is $" + str(price) + ".")