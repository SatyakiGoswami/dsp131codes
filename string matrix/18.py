def remove_ith_character(string, i):
    return string[:i] + string[i+1:]
original_string = "example"
i = 3  # Indexing starts from 0, so the 3rd character is at index 2
modified_string = remove_ith_character(original_string, i)
print("Original string:", original_string)
print("Modified string:", modified_string)