def print_duplicates(lst):
    counts = {}
    duplicates = []

    for num in lst:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    for num, count in counts.items():
        if count > 1:
            duplicates.append(num)

    return duplicates
my_list = [1, 2, 3, 2, 4, 5, 3, 6, 6, 7]
duplicate_numbers = print_duplicates(my_list)
print("Duplicate numbers in the list:", duplicate_numbers)