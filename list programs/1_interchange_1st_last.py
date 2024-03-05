def interchange_first_last(lst):
    if len(lst) < 2:
        return lst
    else:
        lst[0], lst[-1] = lst[-1], lst[0]
        return lst

# Example usage:
my_list = [1, 2, 3, 4, 5]
interchanged_list = interchange_first_last(my_list)
print("Original List:", my_list)
print("Interchanged List:", interchanged_list)