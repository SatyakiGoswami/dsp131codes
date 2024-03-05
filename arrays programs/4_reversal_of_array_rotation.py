def reverse_array(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate_array(arr, d):
    n = len(arr)
    # To handle cases where d is greater than the array length
    d = d % n
    # Rotate the array using reversal algorithm
    reverse_array(arr, 0, d - 1)
    reverse_array(arr, d, n - 1)
    reverse_array(arr, 0, n - 1)
    return arr

# Example usage:
array = [1, 2, 3, 4, 5]
positions = 2
print("Original array:", array)
print("Array after left rotation by", positions, "positions:", rotate_array(array, positions))