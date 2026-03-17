text = input("Enter string: ")
width = int(input("Enter total width: "))

# Calculate padding, ensuring it never goes below 0
padding = max(0, width - len(text))
result = text + (" " * padding)

print(f"Result: '{result}'")