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