def all_pairs_combinations(tuple1, tuple2):
    pairs = []
    for elem1 in tuple1:
        for elem2 in tuple2:
            pairs.append((elem1, elem2))
    return pairs

tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
pairs = all_pairs_combinations(tuple1, tuple2)
print("All pairs combinations:", pairs)