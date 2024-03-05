def find_remainder(arr, n):
    result = 1
    for num in arr:
        result = (result * num) % n
    return result

# Example usage:
array = [1, 2, 3, 4, 5]
divisor = 7
print("Array:", array)
print("Divisor:", divisor)
print("Remainder of array multiplication divided by", divisor, ":", find_remainder(array, divisor))