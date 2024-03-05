def print_even_numbers(start, end):
    even_numbers = [num for num in range(start, end+1) if num % 2 == 0]
    return even_numbers
start_range = 1
end_range = 20
even_numbers = print_even_numbers(start_range, end_range)
print("Even numbers in the range:", even_numbers)