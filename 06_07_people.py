# Dictionary for Avery
person1 = {
    'first_name': 'Avery',
    'last_name': 'James',
    'age': 18,
    'city': 'New York'
}

# Dictionary for Jordan
person2 = {
    'first_name': 'Jordan',
    'last_name': 'Wells',
    'age': 47,
    'city': 'Los Angeles'
}

# Dictionary for Taylor
person3 = {
    'first_name': 'Taylor',
    'last_name': 'Squid',
    'age': 22,
    'city': 'Pheonix'
}

# List that holds all the people
people = [person1, person2, person3]

# Loops through the list of people
for person in people:
    # Print each piece of info
    print("First name:", person['first_name'])
    print("Last name:", person['last_name'])
    print("Age:", person['age'])
    print("City:", person['city'])
    print()