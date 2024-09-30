# Variable
car = 'subaru'

# Test 1 true
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

# Test 2 false
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

# Test 3 true
print("\nIs car.lower() == 'subaru'? I predict True.")
print(car.lower() == 'subaru')

# Test 4 false
print("\nIs car == 'Toyota'? I predict False.")
print(car == 'Toyota')

# Test 5 true
print("\nIs car != 'ford'? I predict True.")
print(car != 'ford')

# Test 6 true
print("\nIs car == 'subaru' and len(car) == 6? I predict True.")
print(car == 'subaru' and len(car) == 6)

# Test 7 false
print("\nIs car == 'dodge'? I predict False.")
print(car == 'dodge')

# Test 8 true
print("\nIs car in ['subaru', 'GMC', 'hyundai']? I predict True.")
print(car in ['subaru', 'GMC', 'hyundai'])

# Test 9 true
print("\nIs car == 'Bentley' or car == 'subaru'? I predict True.")
print(car == 'Bentley' or car == 'subaru')

# Test 10 false
print("\nIs car == 'Kia'? I predict False.")
print(car == 'Kia')
