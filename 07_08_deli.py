# Sandwich orders list
sandwich_Orders = ['club', 'veggie', 'ham', 'cheese', 'turkey']
# Empty list for finished sandwiches
finished_Sandwiches = []

# Loop through list of sandwich orders
for sandwich in sandwich_Orders:
    print("I made your " + sandwich + " sandwich.")
    # Moving sandwich to the finished sandwiches list
    finished_Sandwiches.append(sandwich)

# Print a message that says each sandwich that was made
print("\nAll sandwiches made:")
for finished_Sandwich in finished_Sandwiches:
    print(finished_Sandwich)