

text = input("Enter string with leading spaces: ")
start_index = 0

for i in range(len(text)):
    if text[i] != " ":
        start_index = i
        break
else:
    start_index = len(text) # Handles string with only spaces

print(f"Result: '{text[start_index:]}'")