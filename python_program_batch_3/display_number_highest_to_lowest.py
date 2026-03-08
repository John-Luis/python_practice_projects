
def numbers_highest_to_lowest():

    numbers = []

    while True:
        data = input("Enter a number (or any letter to stop): ")

        # Check if the input is a number
        if data.isdigit():
            numbers.append(int(data))
        else:
            break

        numbers.sort()

        print("Numbers from lowest to highest:")
        print(numbers)

numbers_highest_to_lowest()