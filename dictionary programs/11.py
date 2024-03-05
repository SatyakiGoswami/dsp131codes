
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
for key, value in dict1.items():
    dict2[key] = value

print(dict2)