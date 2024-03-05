def find_second_largest(lst):
    if len(lst) < 2:
        return "List should have at least two elements"
    
    largest = max(lst[0], lst[1])
    second_largest = min(lst[0], lst[1])

    for num in lst[2:]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    return second_largest

my_list = [5, 2, 8, 1, 9, 3]
second_largest_number = find_second_largest(my_list)
print("The second largest number in the list is:", second_largest_number)