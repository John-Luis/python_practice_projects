

def count_odd_numbers():

    odd_count = 0
    for i in range(10):
        num = int(input(f"Enter number {i + 1}: "))
        if num % 2 != 0:
            odd_count += 1
    print(f"Total Odd Numbers: {odd_count}")

count_odd_numbers()