# Guests
guests = ["Charles Darwin", "Abraham Lincoln", "Marilyn Monroe"]

# Invite
for guest in guests:
    print(f"{guest}, please join me for dinner this evening at 6:30pm. \nLove, \nJackie Arteaga")

# Unable to go
not_Attending = "Charles Darwin"
print(f"Sadly, {not_Attending} won't be able to make it. \n")

# Remove and eplace
guests.remove(not_Attending)
new_Person = "Princess Diana"
guests.append(new_Person)

# Newer invites
for guest in guests:
    print(f"{guest}, please join me for dinner this evening at 6:30pm. \nLove, \nJackie Arteaga")