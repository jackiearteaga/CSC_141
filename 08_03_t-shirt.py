def make_shirt(size, message):
    print("The shirt size is " + size + " and the message printed is: '" + message + "'.")

# Function called using positional arguments
make_shirt("Small", "Python is cool!")

# Function called using keyword arguments
make_shirt(message="Python Power!", size="Medium")
