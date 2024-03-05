my_dict = {'c': 3, 'a': 1, 'b': 2}

sorted_dict_by_value = {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1])}
print(sorted_dict_by_value)