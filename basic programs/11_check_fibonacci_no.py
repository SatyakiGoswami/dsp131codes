
def is_perfect_square(n):
    root = int(n ** 0.5)
    return root * root == n

def is_fibonacci(number):

    return is_perfect_square(5 * number * number + 4) or is_perfect_square(5 * number * number - 4)


number = int(input("Enter a number to check if it's a Fibonacci number: "))


if is_fibonacci(number):
    print(number, "is a Fibonacci number.")
else:
    print(number, "is not a Fibonacci number.")