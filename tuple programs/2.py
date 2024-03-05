
my_tuple = (5, 3, 9, 1, 7, 2, 8, 4, 6)

k = 3
max_k_elements = sorted(my_tuple)[-k:]
min_k_elements = sorted(my_tuple)[:k]

print(f"Maximum {k} elements:", max_k_elements)
print(f"Minimum {k} elements:", min_k_elements)