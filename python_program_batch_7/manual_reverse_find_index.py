


text = input("Enter main string: ")
sub = input("Enter substring to find from end: ")
sub_len = len(sub)
found_index = -1

for i in range(len(text) - sub_len, -1, -1):
    if text[i:i+sub_len] == sub:
        found_index = i
        break

if found_index != -1:
    print(f"Last index: {found_index}")
else:
    print("Substring not found.")