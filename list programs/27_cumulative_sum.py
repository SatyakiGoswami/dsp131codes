def cumulative_sum(lst):
    cum_sum = 0
    cumulative_list = []
    for num in lst:
        cum_sum += num
        cumulative_list.append(cum_sum)
    return cumulative_list

my_list = [1, 2, 3, 4, 5]
cumulative_result = cumulative_sum(my_list)
print("Cumulative sum of the list:", cumulative_result)