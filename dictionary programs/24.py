from collections import Counter

def make_string_with_deletion_and_rearrangement(str1, str2):

    count_str1 = Counter(str1)
    count_str2 = Counter(str2)
    common_chars = (count_str1 & count_str2)

    result_string = ''.join(sorted(common_chars.elements()))

    return result_string

str1 = "aabbcc"
str2 = "abb"
result = make_string_with_deletion_and_rearrangement(str1, str2)
print("Resulting string:", result)