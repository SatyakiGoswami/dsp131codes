
tuple_of_lists = ([1, 2, 3], [4, 5], [6, 7, 8])

flattened_tuple = tuple(element for sublist in tuple_of_lists for element in sublist)

print("Flattened tuple:", flattened_tuple)