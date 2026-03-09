


def average ():
    total_sum = 0
    count = 0

    while True:
        data = input("Enter a number (or a letter to stop): ")

        # Check if the input is a valid number (handles decimals)
        if data.replace('.', '', 1).isdigit():
            number = float(data)
            total_sum += number
            count += 1
        else:
            # If it's not a number, stop the loop
            break

    # Calculate and print the average only if at least one number was entered
    if count > 0:
        average = total_sum / count
        print(f"Average: {average}")
    else:
        print("No numbers were entered.")
average()