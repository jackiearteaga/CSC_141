import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides  # Default amount of sides is 6

    def roll_die(self):
        return random.randint(1, self.sides)

# 6-sided die
six_sided_die = Die()

# Roll the die 10 times
print("Rolling a 6-sided die:")
for _ in range(10):
    print(six_sided_die.roll_die())

# 10-sided die
ten_sided_die = Die(sides=10)

# Roll th die 10 times
print("\nRolling a 10-sided die:")
for _ in range(10):
    print(ten_sided_die.roll_die())

# 20-sided die
twenty_sided_die = Die(sides=20)

# Roll the die 10 times
print("\nRolling a 20-sided die:")
for _ in range(10):
    print(twenty_sided_die.roll_die())