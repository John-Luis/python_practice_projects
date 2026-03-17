

fullname = input("Input Name with leading spaces: ")

def trim_leading_spaces(text):
    print(f"Before: {text}")
    print(f"Output: {text.lstrip()}")

trim_leading_spaces(fullname)

