
numbers = []
print("Enter numbers (input any non-number to stop):")

while True:
    try:
        num = float(input("> "))
        numbers.append(num)
    except ValueError:
        break

if numbers:
    print(f"Highest number: {max(numbers)}")