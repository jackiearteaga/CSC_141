# Existing dictionary of favorite_languages
favorite_languages = { 
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

# List of who should take the poll
people_to_poll = ['jen', 'sarah', 'tommy', 'anne', 'phil', 'ben']

# Loop through list of people
for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you, {person.title()}, for responding!\n")
    else:
        print(f"Hi {person.title()}, please take our favorite languages poll!\n")