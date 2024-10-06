# Dictionary for a dog
pet1 = {
    'kind': 'Dog',
    'owner': 'Aless'
}

# Dictionary for a cat
pet2 = {
    'kind': 'Cat',
    'owner': 'Jack'
}

# Dictionary for a parrot
pet3 = {
    'kind': 'Parrot',
    'owner': 'Alisson'
}

# List that holds all the pets
pets = [pet1, pet2, pet3]

# Loops through the list of pets
for pet in pets:
    # Prints each piece of information
    print("Kind of animal:", pet['kind'])
    print("Owner's name:", pet['owner'])
    print()