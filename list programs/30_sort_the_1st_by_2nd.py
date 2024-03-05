def sort_list_by_another_list(list1, list2):

    combined_lists = zip(list2, list1)
    sorted_combined_lists = sorted(combined_lists)
    sorted_list1 = [elem[1] for elem in sorted_combined_lists]
    
    return sorted_list1
list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]
sorted_list1 = sort_list_by_another_list(list1, list2)
print("Sorted list1 using list2 as keys:", sorted_list1)