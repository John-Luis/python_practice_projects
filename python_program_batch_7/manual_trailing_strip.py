
text = input("enter text")
count = 0

for i in range (len(text)-1,-1,-1):
    if text[i] != " ":
        count = 1 + i
        break

print(text[:count])
    