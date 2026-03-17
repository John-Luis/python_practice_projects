

text = input("Enter main string: ")
sub = input("Enter substring to count: ")
count = 0
sub_len = len(sub)

for i in range(len(text) - sub_len + 1):
    if text[i:i+sub_len] == sub:
        count += 1

print(f"Occurrences: {count}")