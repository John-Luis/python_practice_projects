
def bigger_number():
    # Adding a try-except block prevents the program from crashing on typos
    try:
        ask_number_1 = float(input("Enter your first number: "))
        ask_number_2 = float(input("Enter your second number: "))

        if ask_number_1 > ask_number_2:
            print(f"{ask_number_1} is the bigger number")
        elif ask_number_2 > ask_number_1:
            print(f"{ask_number_2} is the bigger number")
        else:
            print("Both numbers are equal.")
    except ValueError:
        print("Invalid input! Please enter numbers only.")

bigger_number()