from collections import OrderedDict

def kth_non_repeating_char(input_str, k):
    char_count = OrderedDict()

    for char in input_str:
        char_count[char] = char_count.get(char, 0) + 1

    non_repeating_chars = [char for char, count in char_count.items() if count == 1]

    return non_repeating_chars[k - 1] if k <= len(non_repeating_chars) else None

input_str = "aabbcdde"
k = 3
result = kth_non_repeating_char(input_str, k)
print(f"The {k}'th non-repeating character is:", result)