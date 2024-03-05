from collections import OrderedDict

def check_order(string, pattern):
    char_order = OrderedDict.fromkeys(string)
    pattern_index = 0
    for char in char_order:
        if pattern_index < len(pattern) and char == pattern[pattern_index]:
            pattern_index += 1
    return pattern_index == len(pattern)

string = "hello world"
pattern = "llo"
print(check_order(string, pattern))