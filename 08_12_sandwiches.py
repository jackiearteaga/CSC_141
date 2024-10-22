def make_sandwich(*items):
    print("The sandwich you ordered contains:")
    for item in items:
        print(item)
    print()

# Call function three times with different numbers of arguments
make_sandwich("lettuce", "pepperoni", "mayo")
make_sandwich("cheese", "ham")
make_sandwich("peanut butter", "nutella", "banana", "strawberries")