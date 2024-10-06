# Dictionary for favorite places
favorite_places = {
    'Aless': ['Paris', 'Chicago', 'Italy'],
    'Betty': ['London', 'Venezuela'],
    'Josh': ['New York', 'Melbourne', 'Perth']
}

# Loops through the dictionary
for name, places in favorite_places.items():
    # Prints each person's name
    print(name + "'s favorite places are:\n")
    # Prints each favorite place
    for place in places:
        print(place)
    print()
