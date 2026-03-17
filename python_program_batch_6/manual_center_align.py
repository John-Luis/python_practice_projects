text = input("Enter string: ")
width = int(input("Enter total width: "))

text = input("Enter string: ")
width = int(input("Enter total width: "))

# Calculate the total space needed (at least 0)
total_pad = max(0, width - len(text))

# Split the padding: half for the left, the remainder for the right
left_pad = total_pad // 2
right_pad = total_pad - left_pad

result = (" " * left_pad) + text + (" " * right_pad)

print(f"Result: '{result}'")