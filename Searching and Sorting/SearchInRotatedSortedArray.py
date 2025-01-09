def search(nums, target):
    low, high = 0, len(nums) - 1

    while low <= high:
        #mid = low + (high - low) // 2
        mid = (low+high)//2

        # Check if mid is the target
        if nums[mid] == target:
            return mid

        # Determine which half is sorted
        if nums[low] <= nums[mid]:  # Left half is sorted
            if nums[low] <= target < nums[mid]:  # Target is in the left half
                high = mid - 1
            else:  # Target is in the right half
                low = mid + 1
        else:  # Right half is sorted
            if nums[mid] < target <= nums[high]:  # Target is in the right half
                low = mid + 1
            else:  # Target is in the left half
                high = mid - 1

    return -1  # Target not found

nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(search(nums,target))