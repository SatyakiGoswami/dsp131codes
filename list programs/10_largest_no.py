def find_largest_number(numbers):
    if not numbers:
        return None
    largest =numbers[0]
    for num in numbers :
        if num > largest:
            largest=num
    return largest
numbers=[10,8,22,13,7]
largest_number=find_largest_number(numbers)
print("The largest number in the list is :",large)