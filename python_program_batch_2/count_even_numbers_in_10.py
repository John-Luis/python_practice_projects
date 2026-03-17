even_count = 0

# We use a counter variable initialized at 0. For each of the 10 inputs, we check if num % 2 == 0. If true, we increment the counter.
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    if num % 2 == 0:
        even_count += 1

print(f"Even numbers found: {even_count}")