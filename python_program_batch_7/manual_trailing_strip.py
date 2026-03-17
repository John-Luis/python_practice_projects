



text = input("Enter a string with spaces at the end: ")
end_index = len(text)

def manual_trailing_strip(text):
    for i in range(len(text) - 1, -1, -1):
        if text[i] != " ":
            end_index = i + 1
            break
    else:
        # If the string was only spaces
        end_index = 0

    # A logic to show spaces as underscore for exhibition
    # replacing the spaces with underscore '_', only for visuals.

    visible_before = text.replace(" ", "_")


    print(f"Before:{text}\nAfter:{text[:end_index]}")


manual_trailing_strip(text)

