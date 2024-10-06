# Example from "A Dictionary in a Dictionary" section
# Original users dictionary with added keys
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        'age': 76,
        'favorite_books': ['The World as I See It', 'Relativity: The Special and General Theory']
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        'age': 66,
        'favorite_books': ['Radioactive', 'Pierre Curie']
    },
}

# Loops through the users
for username, user_info in users.items():
    print(f"\nUsername: {username}")  # Prints the username
    full_name = f"{user_info['first']} {user_info['last']}"  # Full name
    location = user_info['location']  # Location
    age = user_info['age']  # Age (added by me)
    favorite_books = user_info['favorite_books']  # Favorite books (added by me)

    # Prints the user's info
    print(f"\tFull Name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
    print(f"\tAge: {age}")
    print("\tFavorite Books:")
    
    # New loop that prints each favorite book
    for book in favorite_books:
        print(f"\t{book}")