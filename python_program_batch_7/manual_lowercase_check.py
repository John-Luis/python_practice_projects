

text = input("enter text")
is_lower = True
has_word = False

for char in text:
    if "a" <= char <= "z":
        has_word = True
    elif "A"<= char <= "Z":
        is_lower = False
        
print(is_lower and has_word)
