



text = input("Enter a string with spaces at the end: ")
end_index = len(text)

def manual_trailing_strip(text):
    for i in range(len(text) - 1, -1, -1):
        if text[i] != " ":
            end_index = i + 1
            break

    print(f"Before:{text}\nAfter:{text[:end_index]}")



manual_trailing_strip(text)

