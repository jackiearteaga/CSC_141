# Using exercise 5_10 as an example
# Current usernames
current_users = ['cody', 'april', 'charles', 'fay', 'dallas']

# New usernames
new_users = ['Tuna', 'Max', 'Cody', 'Tyson', 'April']

# List of lowercase current usernames for comparison
# This allows for case-insensitive username checking
lowercase_current_users = [user.lower() for user in current_users]

# Check for available usernames
for new_user in new_users:
    # Using lower() method to compare usernames case-insensitively
    if new_user.lower() in lowercase_current_users:
        # User is informed that the username is taken
        print(f"Sorry, the username '{new_user}' has already been taken. Please enter a new username.")
    else:
        # User is informed that the username is available
        print(f"The username '{new_user}' is available.")
