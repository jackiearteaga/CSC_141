import random

# List with series of 10 numbers and 5 letters
lottery_items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Randomly select 4 items
winning_combination = random.sample(lottery_items, 4)

# Winning numbers
print("The winning numbers are:", winning_combination)
print("Any ticket matching these 4 numbers or letters wins a prize!")
