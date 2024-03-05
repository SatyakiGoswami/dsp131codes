
list_of_dicts = [
    {'name': 'John', 'age': 30},
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 35}
]

sorted_list = sorted(list_of_dicts, key=lambda x: x['age'])

print(sorted_list)