def nested_tuple_to_dict(nested_tuple):
    custom_dict = {}
    for key, value in nested_tuple:
        if isinstance(value, tuple):
            custom_dict[key] = nested_tuple_to_dict(value)
        else:
            custom_dict[key] = value
    return custom_dict

nested_tuple = (('a', 1), ('b', 2), ('c', (('d', 3), ('e', 4))))
custom_dict = nested_tuple_to_dict(nested_tuple)

print("Custom key dictionary:")
print(custom_dict)