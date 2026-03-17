
fullname = input("Input fullname: ")
# Lowercase everything first, then swap spaces for underscores
snake_case = fullname.lower().replace(" ", "_")
print(f"Output: {snake_case}")