


text = input("enter string")
sub = input("enter substring")

for i in range (len(text) - len(sub), -1, -1):
    if text[i:i+len(sub)] == sub:
        print(i)
