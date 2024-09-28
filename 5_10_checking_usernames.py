# Current usernames
current_users = ['cody', 'april', 'charles', 'fay', 'dallas']

# New usernames
new_users = ['Tuna', 'Max', 'Cody', 'Tyson', 'April']

# List of lowercase current usernames for comparison
lowercase_current_users = [user.lower() for user in current_users]

# Check for available usernames
for new_user in new_users:
    if new_user.lower() in lowercase_current_users:
        print(f"Sorry, the username '{new_user}' has already been taken. Please enter a new username.")
    else:
        print(f"The username '{new_user}' is available.")