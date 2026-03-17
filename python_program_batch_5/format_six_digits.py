
number = input("Input a number (0-1000): ")

def format_six_number(number):
    print(f"Before: {number:>6}")
    print(f"Output: {number.zfill(6)}")

format_six_number(number)
