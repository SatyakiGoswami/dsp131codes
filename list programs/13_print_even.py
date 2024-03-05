def print_even_numbers(lst):
    even_numbers = [num for num in lst if num % 2 == 0]
    return even_numbers

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = print_even_numbers(my_list)
print("Even numbers in the list:", even_numbers)