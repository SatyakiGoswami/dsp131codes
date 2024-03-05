def find_sum(arr):
    total_sum = 0
    for num in arr:
        total_sum += num
    return total_sum

# Example usage:
array = [1, 2, 3, 4, 5]
print("Sum of the array:", find_sum(array))