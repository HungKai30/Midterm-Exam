# Enter a non-negative integer
n = int(input("Enter a non-negative integer: "))

# Check if the number is valid
if n < 0:
    print("Invalid input. Please enter a non-negative integer.")
else:
    # Calculate factorial
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i

    # Print the result
    print(f"{n}! = {factorial}")
