list_of_tuples = [(1, 2), (), (3, 4), (), (), (5, 6), ()]

filtered_list = [tup for tup in list_of_tuples if tup]

print(filtered_list)