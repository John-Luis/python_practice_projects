result = float(input("Enter number 1: "))

for i in range(2, 11):
    num = float(input(f"Enter number {i}: "))
    result -= num

print(f"Final Result: {result}")