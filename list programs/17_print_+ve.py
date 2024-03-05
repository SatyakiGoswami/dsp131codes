def print_positive_numbers(lst):
    positive_numbers = [num for num in lst if num > 0]
    return positive_numbers
my_list = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]
positive_numbers = print_positive_numbers(my_list)
print("Positive numbers in the list:", positive_numbers)