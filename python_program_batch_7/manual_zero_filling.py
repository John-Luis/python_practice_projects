

text = input("Enter number/string: ")
width = int(input("Enter total width: "))

zeros = width - len(text)
result = ("0" * zeros + text) \
    if zeros > 0 \
    else text

print(f"Result: {result}")