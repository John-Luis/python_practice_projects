

text = input("Enter main string: ")
sub = input("Enter substring to find: ")
found_index = -1

for i in range(len(text) - len(sub) + 1):
    if text[i:i+len(sub)] == sub:
        found_index = i
        break

print(f"First index: {found_index}")