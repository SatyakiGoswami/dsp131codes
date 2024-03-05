my_dict = {'c': 3, 'a': 1, 'b': 2}

sorted_dict_by_key = {k: my_dict[k] for k in sorted(my_dict.keys())}
print(sorted_dict_by_key)