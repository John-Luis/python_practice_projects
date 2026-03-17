

text = input("Enter main string: ")
suffix = input("Enter suffix to remove: ")

# Check if the text ends with the suffix
def manual_suffix_remover(text):
    if suffix and text.endswith(suffix):
        result = text[:-len(suffix)]
    else:
        result = text

    print(f"Result: {result}")
    
manual_suffix_remover(text)