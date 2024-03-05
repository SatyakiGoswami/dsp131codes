
def sum_of_squares(n):
    return sum(i ** 2 for i in range(1, n + 1))

n = int(input("Enter the value of n: "))

result = sum_of_squares(n)


print(f"The sum of squares of the first {n} natural numbers is: {result}")