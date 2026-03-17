

text = input("Enter string: ")
result = ""

for char in text:
    #using the ascii value... the lowercase letter were shifted to uppercase version by ascii value being 32 higher.
    if 'a' <= char <= 'z':
        result += chr(ord(char) - 32)
    else:
        result += char

print(f"Result: {result}")