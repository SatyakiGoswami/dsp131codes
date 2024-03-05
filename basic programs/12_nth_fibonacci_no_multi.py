
def fibonacci(n):
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return b

def nth_multiple_in_fibonacci(number, n):
    count = 0
    i = 1
    while count < n:
        fib_number = fibonacci(i)
        if fib_number % number == 0:
            count += 1
            if count == n:
                return fib_number
        i += 1
    return None

number = int(input("Enter the number: "))
n = int(input("Enter the value of n for the nth multiple: "))

result = nth_multiple_in_fibonacci(number, n)
if result:
    print(f"The {n}th multiple of {number} in the Fibonacci series is:", result)
else:
    print(f"No {n}th multiple of {number} found in the Fibonacci series.")