def count_matching_characters(string1, string2):
    set1 = set(string1)
    set2 = set(string2)
    common_characters_count = len(set1.intersection(set2))
    return common_characters_count
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

matching_characters_count = count_matching_characters(string1, string2)
print("Number of matching characters:", matching_characters_count)