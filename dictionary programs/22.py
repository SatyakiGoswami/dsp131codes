def count_frequencies(input_list):
    frequency_dict = {}
    for item in input_list:
        frequency_dict[item] = frequency_dict.get(item, 0) + 1

    return frequency_dict

input_list = [1, 2, 3, 1, 2, 1, 3, 4, 5, 4, 3, 2, 1]
frequency_dict = count_frequencies(input_list)
print("Frequencies:", frequency_dict)