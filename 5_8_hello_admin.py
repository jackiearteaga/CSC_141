# Usernames
usernames = ['Cody', 'April', 'Admin', 'Charles', 'Todd']

# Checks for username "admin"
for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")