def sortInWave(arr, n):
    # First, sort the array
    arr.sort()

    # Then, swap adjacent elements to form a wave
    for i in range(0, n-1, 2):
        arr[i], arr[i+1] = arr[i+1], arr[i]

# Example usage
arr = [10, 90, 49, 2, 1, 5, 23]
n = len(arr)
sortInWave(arr, n)

# Printing the array in wave form
for i in range(n):
    print(arr[i], end=" ")
