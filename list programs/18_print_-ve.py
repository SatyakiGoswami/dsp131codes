def print_negative_numbers(lst):
    negative_numbers = [num for num in lst if num < 0]
    return negative_numbers
my_list = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]
negative_numbers = print_negative_numbers(my_list)
print("Negative numbers in the list:", negative_numbers)