# Variables
car = 'subaru'
foods = ['pizza', 'pasta', 'salad']
age = 18

# Tests for equality and inequality with strings
# True
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

# True
print("\nIs car != 'mercedes'? I predict True.")
print(car != 'mercedes')

# Tests using the lower() method
# True
print("\nIs car.lower() == 'subaru'? I predict True.")
print(car.lower() == 'subaru')

# False
print("\nIs car.lower() == 'SUBARU'? I predict False.")
print(car.lower() == 'SUBARU')

# Numerical tests
# True
print("\nIs age == 18? I predict True.")
print(age == 18)

# False
print("\nIs age > 30? I predict False.")
print(age > 30) 

# True
print("\nIs age < 30? I predict True.")
print(age < 30)

# True
print("\nIs age >= 18? I predict True.")
print(age >= 18)

# False
print("\nIs age <= 15? I predict False.")
print(age <= 15)

# Tests using the and keyword
# True
print("\nIs car == 'subaru' and age < 30? I predict True.")
print(car == 'subaru' and age < 30)

# False
print("\nIs car == 'buick' and age < 30? I predict False.")
print(car == 'buick' and age < 30)

# Tests using the or keyword
# True
print("\nIs car == 'subaru' or age > 30? I predict True.")
print(car == 'subaru' or age > 30)

# False
print("\nIs car == 'honda' or age < 15? I predict False.")
print(car == 'honda' or age < 15)

# Test whether an item is in a list
# True
print("\nIs 'pasta' in foods? I predict True.")
print('pasta' in foods)

# False
print("\nIs 'tacos' in foods? I predict False.")
print('tacos' in foods)

# Test whether an item is not in a list
# False
print("\nIs 'pizza' not in foods? I predict False.")
print('pizza' not in foods)

# True
print("\nIs 'rice' not in foods? I predict True.")
print('rice' not in foods)
