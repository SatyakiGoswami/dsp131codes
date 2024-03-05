
def sum_of_cubes(n):
    return sum(i ** 3 for i in range(1, n + 1))

n = int(input("Enter the value of n: "))

result = sum_of_cubes(n)

print(f"The sum of cubes of the first {n} natural numbers is: {result}")