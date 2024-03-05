def left_rotate_array(arr, d):
    n = len(arr)
    # To handle cases where d is greater than the array length
    d = d % n
    # Rotate the array
    rotated_arr = arr[d:] + arr[:d]
    return rotated_arr

# Example usage:
array = [1, 2, 3, 4, 5]
positions = 2
print("Original array:", array)
print("Array after left rotation by", positions, "positions:", left_rotate_array(array, positions))