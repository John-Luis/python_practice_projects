

def manual_is_upper(text):
    #it will check if the string inputted is empty, if is... it will return false
    if not text:
        return False

    for char in text:

        #here the computer is checking if the string inputted is capital or not
        # it checks by the ASCII table.. where the a represents a number up to the z... where the number in between is all lowercase alphabet.
        if 'a' <= char <= 'z':
            return False

    return True

test_string = input("Enter a string: ")
print(f"Is all upppercase?: {manual_is_upper(test_string)}")
