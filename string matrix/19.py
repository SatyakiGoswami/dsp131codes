def split_and_join(string, delimiter):
    substrings = string.split(delimiter)
    new_string = delimiter.join(substrings)
    
    return substrings, new_string

original_string = "This is a sample string"
delimiter = " " 
split_strings, joined_string = split_and_join(original_string, delimiter)

print("Original string:", original_string)
print("Split strings:", split_strings)
print("Joined string:", joined_string)