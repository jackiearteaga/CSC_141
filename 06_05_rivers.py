# Dictionary with rivers and their countries
rivers = {
    'Nile': 'Egypt',
    'Yangtze': 'China',
    'Amazon': 'Brazil'
    
}

# Sentence about each river
for river in rivers:  # Loop through the keys
    country = rivers[river]  # Get the corresponding country
    print(f"The {river} runs through {country}.")

print() # Blank to read better

# Names of each river
print("Rivers:")
for river in rivers:  # Loop through the keys 
    print(river)

print()  # Blank to read better

# Names of each country
print("Countries:")
for country in rivers.values():  # Use .values() to loop through the countries
    print(country)