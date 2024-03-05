
external_list = ['b', 'a', 'c', 'd']

list_of_tuples = [('b', 2), ('a', 5), ('c', 1), ('d', 3)]
sorted_tuples = sorted(list_of_tuples, key=lambda x: external_list.index(x[0]))

print("Sorted list of tuples using the external list:", sorted_tuples)