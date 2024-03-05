def max_frequency_char(string):

    char_frequency = {}


    for char in string:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1


    max_char = ''
    max_freq = 0
    for char, freq in char_frequency.items():
        if freq > max_freq:
            max_char = char
            max_freq = freq

    return max_char


string = "hello world"
max_char = max_frequency_char(string)
print(f"The maximum frequency character in the string '{string}' is '{max_char}'")