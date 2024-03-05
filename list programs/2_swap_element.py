def swap_elements(lst, index1, index2):
    if 0 <= index1 < len(lst) and 0 <= index2 < len(lst):
        lst[index1], lst[index2] = lst[index2], lst[index1]
        return lst
    else:
        print("Invalid indices provided.")
        return lst

# Example usage:
my_list = [1, 2, 3, 4, 5]
index1 = 1
index2 = 3
swapped_list = swap_elements(my_list, index1, index2)
print("Original List:", my_list)
print("Swapped List:", swapped_list)