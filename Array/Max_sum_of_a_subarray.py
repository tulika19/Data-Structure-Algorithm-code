def max_sum_sumarray(arr):
    n = len(arr)  # Find the length
    curr_sum = 0  # Initialize as 0
    max_sum = float('-inf')  # Initialize to negative infinity to handle all negative arrays

    for i in range(0, n):  # Loop from index 0 to n-1
        curr_sum += arr[i]  # Add the current element to the running sum
        max_sum = max(curr_sum, max_sum)  # Update max_sum to the larger of the two

        if curr_sum < 0:  # If the current sum becomes negative, reset it to 0
            curr_sum = 0

    return max_sum

# Test case
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum Subarray Sum:", max_sum_sumarray(arr))


