# Variable with whitespace characters
name = "\t \n Lisa May \n \t"

# Name with whitespace characters
print("Name with whitespace:")
print(name)

# Name with left whitespace removed
print("\nName with left whitespace removed:")
print(name.lstrip())

# Name with right whitespace removed
print("\nName with right whitespace removed:")
print(name.rstrip())

# Both left and right stripped
print("\nName with left and right whitespace removed:")
print(name.strip())