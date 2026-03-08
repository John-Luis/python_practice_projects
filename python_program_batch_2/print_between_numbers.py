

def between_numbers():

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if num1 < num2:
        for i in range(num1 + 1, num2):
            print(i)
    else:
        for i in range(num1 - 1, num2, -1):
            print(i)

between_numbers()