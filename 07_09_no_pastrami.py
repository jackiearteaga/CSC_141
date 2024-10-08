# Sandwich orders list with 'pastrami' x3
sandwich_Orders = ['tuna', 'ham', 'pastrami', 'turkey', 'pastrami', 'veggie', 'pastrami', 'club']
# Empty list for finished sandwiches
finished_Sandwiches = []

# Message saying the deli ran out of pastrami
print("The deli has run out of pastrami sandwiches!")

# Remove all occurrences of 'pastrami'
while 'pastrami' in sandwich_Orders:
    sandwich_Orders.remove('pastrami')

# Loop through the rest of the list of sandwich orders
for sandwich in sandwich_Orders:
    print("I made your " + sandwich + " sandwich.")
    # Moving sandwich to the finished sandwiches list
    finished_Sandwiches.append(sandwich)

# Message listing each sandwich that was made
print("\nAll sandwiches made:")
for finished_Sandwich in finished_Sandwiches:
    print(finished_Sandwich)
