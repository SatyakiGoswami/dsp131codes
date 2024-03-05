
list_of_tuples = [('b', 2), ('a', 5), ('c', 1), ('d', 3)]
sorted_tuples = sorted(list_of_tuples, key=lambda x: x[1])

print("Sorted list of tuples by the second item:", sorted_tuples)