def remove_duplicates(string):
    unique_chars = ""
    for char in string:
        if char not in unique_chars:
            unique_chars += char
    return unique_chars
string = input("Enter a string: ")
unique_string = remove_duplicates(string)
print("String with duplicates removed:", unique_string)