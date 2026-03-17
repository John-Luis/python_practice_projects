text = input("Enter string: ")
result = ""
new_word = True

for char in text:
    if char == " ":
        result += " "
        new_word = True
    elif new_word:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
        new_word = False
    else:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char

print(f"Result: {result}")