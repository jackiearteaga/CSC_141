# Ask user their dinner group size
group_Size = int(input("How many people are in your dinner group? "))

# Check dinner group size
if group_Size > 8:
    print("Please wait for a table.")
else:
    print("Your table is ready!")