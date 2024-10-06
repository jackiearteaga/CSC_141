# Dictionary for cities
cities = {
    'New York': {
        'country': 'USA',
        'population': 8419600,
        'fact': 'It is known as the Big Apple.'
    },
    'Tokyo': {
        'country': 'Japan',
        'population': 13929286,
        'fact': 'It is the most populous city in the world.'
    },
    'Paris': {
        'country': 'France',
        'population': 2148327,
        'fact': 'It is known for the Eiffel Tower.'
    }
}

# Prints each city and its information
for city, info in cities.items():  # Loops through each city
    print("City:", city)  # Prints the city name
    print("Country:", info['country'])  # Prints the country
    print("Population:", info['population'])  # Prints the population
    print("Fact:", info['fact'])  # Prints a fact about the city
    print()
