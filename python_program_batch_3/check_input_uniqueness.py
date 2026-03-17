history = []
print("Enter numbers (input any letter to stop):")

while True:
    try:
        num = float(input("> "))
        if num in history:
            print("Duplicate")
        else:
            print("Unique")
            history.append(num)
    except ValueError:
        break