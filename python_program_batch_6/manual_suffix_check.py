text = input("Enter string: ")
suffix = input  ("Enter suffix to check: ")

def manual_suffix_check(text,suffix):
    if len(suffix) == 0:
        match = True
    else:
        match = text[-len(suffix):] == suffix

    print(f"Ends with '{suffix}': {match}")

manual_suffix_check(text,suffix)