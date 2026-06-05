

text = input("enter text")
sub = input("enter string")

for i in range(len(text)-len(sub)+1):
    if text[i:i+len(sub)] == sub:
        print(i)
        