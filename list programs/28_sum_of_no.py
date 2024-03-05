def sum_of_digits(number):
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total

def sum_of_digits_in_list(lst):
    total_sum = 0
    for num in lst:
        total_sum += sum_of_digits(num)
    return total_sum

my_list = [123, 45, 678, 90]
total_sum_of_digits = sum_of_digits_in_list(my_list)
print("Sum of digits in the list:", total_sum_of_digits)