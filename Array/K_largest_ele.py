import heapq

def findKthLargest(nums, k):
    # Min-heap to store the k largest elements
    min_heap = []
    
    # Iterate through the array
    for num in nums:
        # Push the current number into the heap
        heapq.heappush(min_heap, num)
        # If the heap size exceeds k, remove the smallest element
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    
    # The root of the heap is the k-th largest element
    return min_heap[0]

# Example Usage
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(findKthLargest(nums, k))  # Output: 5

nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
print(findKthLargest(nums, k))  # Output: 4
