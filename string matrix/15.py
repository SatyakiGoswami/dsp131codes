import re

def contains_special_characters(string):
    special_char_pattern = r'[^a-zA-Z0-9\s]'  

    if re.search(special_char_pattern, string):
        return True
    else:
        return False

test_string = "Hello! How are you?"
if contains_special_characters(test_string):
    print(f"The string '{test_string}' contains special characters.")
else:
    print(f"The string '{test_string}' does not contain special characters.")