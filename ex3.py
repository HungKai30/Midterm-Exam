#kai

#chung ta nhap input vao day
input_str = input("Enter integers separated by spaces: ")
arr = list(map(int, input_str.split()))
n = len(arr)

print("\nStarting Bubble Sort...\n")

for i in range(n):
    swapped = False
    print(f"Pass {i + 1}:")
    for j in range(0, n - i - 1):
        print(f"  Comparing {arr[j]} and {arr[j + 1]}")
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True
            print(f"  => Swapped: {arr}")
        else:
            print("  => No swap needed")
    
    #in ra sau moi lan doi
    print(f"Array after pass {i + 1}: {arr}\n")

    if not swapped:
        break


print("Sorted array:", arr)
