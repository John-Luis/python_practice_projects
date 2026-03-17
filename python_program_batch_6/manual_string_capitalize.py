text = input("Enter string: ")
result = ""

for i in range(len(text)):
    char = text[i]
    ascii_val = ord(char)

    if i == 0 and 'a' <= char <= 'z':
        # Uppercase the first character
        result += chr(ascii_val - 32)
    elif i > 0 and 'A' <= char <= 'Z':
        # Lowercase everything else
        result += chr(ascii_val + 32)
    else:
        # Keep it as is (already correct or not a letter)
        result += char

print(f"Result: {result}")