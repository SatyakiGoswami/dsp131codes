def print_odd_numbers(start, end):
    odd_numbers = [num for num in range(start, end+1) if num % 2 != 0]
    return odd_numbers
start_range = 1
end_range = 20
odd_numbers = print_odd_numbers(start_range, end_range)
print("Odd numbers in the range:", odd_numbers)