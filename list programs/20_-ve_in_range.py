def print_negative_numbers(start, end):
    negative_numbers = [num for num in range(start, end+1) if num < 0]
    return negative_numbers

start_range = -5
end_range = 5
negative_numbers = print_negative_numbers(start_range, end_range)
print("Negative numbers in the range:", negative_numbers)