# 1 - 9 listed
numbers = list(range(1, 10))

# Loop through numbers
for number in numbers:
    if number == 1:
        ordinal = "1st"
    elif number == 2:
        ordinal = "2nd"
    elif number == 3:
        ordinal = "3rd"
    else:
        ordinal = f"{number}th" # Any other number will have "th" at the end    
    
    # Ordinal number
    print(ordinal)
