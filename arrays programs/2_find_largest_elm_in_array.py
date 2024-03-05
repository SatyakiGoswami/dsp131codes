def find_largest(arr):
    if len(arr) == 0:
        return None
    
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest

# Example usage:
array = [5, 3, 9, 1, 7, 2]
print("Largest element in the array:", find_largest(array))