numbers = []
print("Enter numbers (input any non-number to stop):")

while True:
    try:
        num = float(input("> "))
        numbers.append(num)
    except ValueError:
        break

if numbers:
    numbers.sort(reverse=True)
    print(f"Sorted (Highest to Lowest): {numbers}")