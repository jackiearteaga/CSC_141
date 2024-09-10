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