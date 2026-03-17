
fullname = input("Input fullname: ")
# Capitalize each word first, then remove spaces
pascal_case = fullname.title().replace(" ", "")
print(f"Output: {pascal_case}")