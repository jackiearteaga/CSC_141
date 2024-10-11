def make_shirt(size="Large", message="I love Python"):
    print("The shirt size is " + size + " and the message printed is: '" + message + "'.")

# Large shirt with the default message
make_shirt()

# Medium shirt with the default message
make_shirt(size="Medium")

# Shirt of any size with a diff message
make_shirt(size="Small", message="Hello World :)")