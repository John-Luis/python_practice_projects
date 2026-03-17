
numbers = []
for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

print("Numbers that don't have duplicates:")
for num in numbers:
    if numbers.count(num) == 1:
        print(num)