def split_and_add(arr, k):
    n = len(arr)
    if k > n:
        return arr  # Nothing to do if k is greater than the array length
    return arr[k:] + arr[:k]

# Example usage:
array = [1, 2, 3, 4, 5]
k = 2
print("Original array:", array)
print("Array after splitting and adding the first", k, "elements to the end:", split_and_add(array, k))