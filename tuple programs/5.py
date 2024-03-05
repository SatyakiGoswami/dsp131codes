def closest_pair_to_kth_index(my_tuple, k):
    if k < 0 or k >= len(my_tuple):
        return None
    closest_pair = None
    min_difference = float('inf')
    for element in my_tuple:

        difference = abs(element - my_tuple[k])

        if difference < min_difference:
            closest_pair = (element, my_tuple[k])
            min_difference = difference

    return closest_pair
my_tuple = (1, 3, 6, 9, 12)
k = 2
closest_pair = closest_pair_to_kth_index(my_tuple, k)
print("Closest pair to the {}th index element:".format(k), closest_pair)