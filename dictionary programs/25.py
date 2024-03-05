from collections import Counter

def frequencies_become_same(input_list):

    frequency_counter = Counter(input_list)

    unique_frequencies = set(frequency_counter.values())

    return len(unique_frequencies) == 1


input_list1 = [1, 2, 2, 3, 3, 3]
input_list2 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
input_list3 = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3]

print("Are frequencies in input_list1 the same?", frequencies_become_same(input_list1)) 
print("Are frequencies in input_list2 the same?", frequencies_become_same(input_list2))
print("Are frequencies in input_list3 the same?", frequencies_become_same(input_list3))