
text = input("enter text")
is_upper = True
has_word = False

for char in text:
    if "A" <= char <= "Z":
        has_word = True
    elif "a" <= char <= "z":
        is_upper = False:
        
print(is_upper and has_word)