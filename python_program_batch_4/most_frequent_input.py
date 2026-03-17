numbers = []
print("Enter numbers (input any letter to stop):")

# Part 1: Collect the numbers
while True:
    try:
        user_input = input("> ")
        num = float(user_input)
        numbers.append(num)
    except ValueError:
        break

# Part 2: Find the most frequent
if numbers:
    most_frequent = numbers[0]
    highest_count = 0

    for num in numbers:
        # Count how many times 'num' appears in the whole list
        current_count = numbers.count(num)

        # If this number appears more than our previous record, update it
        if current_count > highest_count:
            highest_count = current_count
            most_frequent = num

    print(f"Number with most duplicates: {most_frequent}")
else:
    print("No numbers were entered.")