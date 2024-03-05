def are_binary_anagrams(num1, num2):
    binary_str1 = bin(num1)[2:]
    binary_str2 = bin(num2)[2:]
    return sorted(binary_str1) == sorted(binary_str2)

# Example usage:
num1 = 5
num2 = 10
print(are_binary_anagrams(num1, num2))

num3 = 7
num4 = 8
print(are_binary_anagrams(num3, num4)) 