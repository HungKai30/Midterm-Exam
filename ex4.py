#kai
n = int(input("Enter the position (n) to find the n-th Fibonacci number: "))

if n < 0:
    print("Invalid input. Please enter a non-negative integer.")
else:

    fib = [0] * (n + 1)

    if n >= 1:
        fib[1] = 1


    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    print(f"The {n}-th Fibonacci number is: {fib[n]}")
