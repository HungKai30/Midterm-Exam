# Fibonacci Sequence using Dynamic Programming

# Input: n
n = int(input("Enter the position (n) to find the n-th Fibonacci number: "))

# Check for valid input
if n < 0:
    print("Invalid input. Please enter a non-negative integer.")
else:
    # Initialize an array to store Fibonacci numbers
    fib = [0] * (n + 1)

    # Base cases
    if n >= 1:
        fib[1] = 1

    # Fill the array using the bottom-up approach
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    # Output the result
    print(f"The {n}-th Fibonacci number is: {fib[n]}")
