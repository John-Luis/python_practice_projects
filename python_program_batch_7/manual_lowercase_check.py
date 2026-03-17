

text = input("Enter string: ")
is_lower = True
has_alpha = False

for char in text:
    if 'A' <= char <= 'Z':
        is_lower = False
        break
    # this is where we use again the ascii value, technically the values in it.
    if 'a' <= char <= 'z':
        has_alpha = True

print(f"Result: {is_lower and has_alpha}")