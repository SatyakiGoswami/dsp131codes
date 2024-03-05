def find_n_largest_elements(lst, n):
    if len(lst) < n:
        return "List has fewer elements than N"
    
    lst.sort(reverse=True)
    return lst[:n]

my_list = [5, 2, 8, 1, 9, 3]
N = 3
n_largest_elements = find_n_largest_elements(my_list, N)
print(f"The {N} largest elements in the list are:", n_largest_elements)