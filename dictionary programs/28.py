def find_keys_by_value(input_dict, target_value):
    keys_list = []
    for key, value in input_dict.items():
        if value == target_value:
            keys_list.append(key)
    return keys_list
my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}
target_value = 1
keys_associated_with_value = find_keys_by_value(my_dict, target_value)
print("Keys associated with value {}: {}".format(target_value, keys_associated_with_value))