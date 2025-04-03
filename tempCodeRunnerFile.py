# Fibonacci Sequence using Dynamic Programming

# Input: n
n = int(input("Enter the position (n) to find the n-th Fibonacci number: "))

# Check for valid input
if n < 0:
    print("Invalid input. Please enter a non-negative integer.")
else:
    # Initialize variables to store Fibonacci numbers
    a, b = 0, 1
    i = 0

    # Use a while loop to calculate the n-th Fibonacci number
    while i < n:
        a, b = b, a + b
        i += 1

    # Output the result
    print(f"The {n}-th Fibonacci number is: {a}")
