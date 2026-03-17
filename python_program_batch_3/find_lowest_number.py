numbers = []
print("Enter numbers (input any letter to stop):")

while True:
    try:
        num = float(input("> "))
        numbers.append(num)
    except ValueError:
        break

if numbers:
    print(f"Lowest number: {min(numbers)}")