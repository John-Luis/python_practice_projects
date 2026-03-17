text = input("Enter string: ")
width = int(input("Enter total width: "))

padding = max(0, width - len(text))
result = (" " * padding) + text

print(f"Result: '{result}'")