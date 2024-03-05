
my_dict = {'c': 3, 'a': 1, 'b': 2}
sorted_keys = sorted(my_dict.keys())
sorted_values = [v for k, v in sorted(my_dict.items(), key=lambda item: item[1])]
sorted_dict = dict(zip(sorted_keys, sorted_values))

print(sorted_dict)