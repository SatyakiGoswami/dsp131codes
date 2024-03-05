def join_tuples_with_similar_initial_elements(tuples_list):
    grouped_tuples = {}
    for tup in tuples_list:
        initial_element = tup[0]
        if initial_element in grouped_tuples:
            grouped_tuples[initial_element].append(tup[1:])
        else:
            grouped_tuples[initial_element] = [tup[1:]]
    result = []
    for key, values in grouped_tuples.items():
        if len(values) > 1:
            joined_tuple = (key,) + tuple(sum(values, ())) 
            result.append(joined_tuple)
        else:
            result.append((key,) + values[0])

    return result

tuples_list = [(1, 'a', 'b'), (2, 'c', 'd'), (1, 'e', 'f'), (3, 'g', 'h'), (2, 'i', 'j')]
joined_tuples = join_tuples_with_similar_initial_elements(tuples_list)
print("Joined tuples:", joined_tuples)