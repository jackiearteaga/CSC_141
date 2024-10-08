# Empty list to store vacation places
dream_Vacations = []

# Poll users
while True:
    vacation = input("If you could visit one place in the world, where would you go? (type 'quit' to finish): ")
    
    # Check if the user wants to quit
    if vacation.lower() == 'quit':
        break
    
    # Add the vacation destination to the list
    dream_Vacations.append(vacation)

# Print the results of poll
print("\nDream Vacation Destinations:")
for destination in dream_Vacations:
    print(destination)
