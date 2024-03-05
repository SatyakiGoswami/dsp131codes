def find_mirror_character(input_str):
    mirror_dict = {
        'A': 'A', 'B': 'D', 'C': 'C', 'D': 'B', 'E': '3',
        'F': 'F', 'G': 'G', 'H': 'H', 'I': 'I', 'J': 'L',
        'K': 'K', 'L': 'J', 'M': 'M', 'N': 'N', 'O': 'O',
        'P': 'Q', 'Q': 'P', 'R': '7', 'S': '2', 'T': 'T',
        'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y',
        'Z': '5', '1': '1', '2': 'S', '3': 'E', '4': '4',
        '5': 'Z', '6': '9', '7': 'R', '8': '8', '9': '6',
        '0': '0', ' ': ' '
    }

    mirror_str = ''

    for char in input_str:
        mirror_str += mirror_dict.get(char, '')

    return mirror_str

input_str = "HELLO"
mirror_str = find_mirror_character(input_str)
print("Mirror string:", mirror_str)