
def fibonacci(n):
    if n <= 0:
        print("Invalid input. Please enter a positive integer.")
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter the value of n to find the nth Fibonacci number: "))

result = fibonacci(n)
if result is not None:
    print("The", n, "th Fibonacci number is:", result)