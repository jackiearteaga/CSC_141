# Empty list
usernames = [] 

# Checks to see if the list is not empty
if not usernames: 
    print("We need to find some users!")
# If not empty, it loops through the list and print the greetings
else:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again.")