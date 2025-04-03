#kai

try:
    n = int(input("Enter a non-negative integer: "))
    if n < 0:
        print("Invalid input. Please enter a non-negative integer.")
    else:
        factorial = 1
        for i in range(2, n + 1):
            factorial *= i
        print(f"{n}! = {factorial}")
except ValueError:
    print("Invalid input. Please enter an integer.")
