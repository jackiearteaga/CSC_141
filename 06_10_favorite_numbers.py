# Favorite numbers
fav_numbers = {
    'Joel': [7, 12, 19],
    'Thomas': [8, 3],
    'Avabelle': [4, 15],
    'Jade': [6, 22, 5],
    'Flint': [3, 9]
}

# Each person's name and their favorite numbers
for name in fav_numbers:  # Loops through each person's name
    print(name + "'s favorite numbers are:")  # Prints the person's name
    for number in fav_numbers[name]:  # Loops through their favorite numbers
        print(str(number))  # Prints each favorite number
    print()
