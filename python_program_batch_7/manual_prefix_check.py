

text = input("Enter string: ")
prefix = input("Enter prefix to check: ")

match = text[:len(prefix)] == prefix
print(f"Starts with '{prefix}': {match}")