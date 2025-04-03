# Bubble Sort in Python with step-by-step output

# Input array from user
input_str = input("Enter integers separated by spaces: ")
arr = list(map(int, input_str.split()))
n = len(arr)

print("\nStarting Bubble Sort...\n")

# Bubble Sort algorithm
for i in range(n):
    swapped = False
    print(f"Pass {i + 1}:")
    for j in range(0, n - i - 1):
        print(f"  Comparing {arr[j]} and {arr[j + 1]}")
        if arr[j] > arr[j + 1]:
            # Swap if elements are in wrong order
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True
            print(f"  => Swapped: {arr}")
        else:
            print("  => No swap needed")
    
    # Print array after each pass
    print(f"Array after pass {i + 1}: {arr}\n")

    # If no elements were swapped, array is sorted
    if not swapped:
        break

# Final result
print("Sorted array:", arr)
