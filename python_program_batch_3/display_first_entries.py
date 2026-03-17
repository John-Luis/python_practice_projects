
numbers = []
for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

seen = []
for num in numbers:
    if num not in seen:
        seen.append(num)

print("Unique list (first entries only):")
print(seen)