def remove_tuples_of_length_k(tuple_list, k):
    return [tup for tup in tuple_list if len(tup) != k]

tuple_list = [(1, 2), ('a', 'b', 'c'), (3, 4, 5), ('x', 'y')]
k = 3
filtered_tuples = remove_tuples_of_length_k(tuple_list, k)
print("Filtered tuples:", filtered_tuples)