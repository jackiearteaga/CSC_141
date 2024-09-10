# Guests
guests = ["Charles Darwin", "Abraham Lincoln", "Marilyn Monroe"]

# Invite
for guest in guests:
    print(f"{guest}, please join me for dinner this evening at 6:30pm. \nLove, \nJackie Arteaga \n")

# Unable to go
not_Attending = "Charles Darwin"
print(f"Sadly, {not_Attending} won't be able to make it. \n")

# Remove and eplace
guests.remove(not_Attending)
new_Person = "Princess Diana"
guests.append(new_Person)

# Newer invites
for guest in guests:
    print(f"{guest}, please join me for dinner this evening at 6:30pm. \nLove, \nJackie Arteaga \n")

# Informing we have a bigger table
print("Great news! A bigger dinner table was found so we can make more room for guests. \n")

# New guests
guests.insert(0, "Paul Walker")
guests.insert(2, "Michael Jackson")
guests.append("Martin Luther King")

# Updated invites
for guest in guests:
    print(f"{guest}, please join me for dinner this evening at 6:30pm. \nLove, \nJackie Arteaga \n")

# Inform them about reduced guest list
print("I'm so sorry guys! We aren't getting the big table in time, so I can only invite two guests! \n")

# Removing guests
print(f" Sorry, {guests.pop()}, you are not invited to dinner anymore. \n")
print(f" Sorry, {guests.pop()}, you are not invited to dinner anymore. \n")
print(f" Sorry, {guests.pop()}, you are not invited to dinner anymore. \n")
print(f" Sorry, {guests.pop()}, you are not invited to dinner anymore. \n")

# Invite to the two guests that will attend.
print("New Invites:")
for guest in guests:
    print(f"Dear {guest}, \nYou are still invited to dinner at 6:30pm. See you then! \nLove, \nJackie Arteaga \n")

# Empty out list
del guests[:]

# Print empty list
print("New invite list:", guests)