def print_positive_numbers(start, end):
    positive_numbers = [num for num in range(start, end+1) if num > 0]
    return positive_numbers
start_range = -5
end_range = 5
positive_numbers = print_positive_numbers(start_range, end_range)
print("Positive numbers in the range:", positive_numbers)