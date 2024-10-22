def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

# Replace
user_profile = build_profile(
    'Jackie',
    'Arteaga',
    location = 'Leesport',
    hobby = 'Baking',
    favorite_colors ='Pink and Green'
)

# User profile printed
print(user_profile)