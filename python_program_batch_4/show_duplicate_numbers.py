numbers = []
for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

duplicates = []
for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print(f"Numbers with duplicates: {duplicates}")