import random

# List containing 10 numbers and 5 letters
lottery_items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Define lottery ticket with 4 random items
my_ticket = random.sample(lottery_items, 4)

print("My lottery ticket is:", my_ticket)

# Number of attempts at 0
attempts = 0

# Loop keeps making combination of numbers until the ticket wins
while True:
    attempts += 1  # Increment number of attempts
    winning_combination = random.sample(lottery_items, 4)

    # Check if winning combination matches ticket
    if winning_combination == my_ticket:
        break  # Exit loop if you have a winning ticket

print(f"Woah! It took {attempts} attempts to win with the ticket {my_ticket}!")