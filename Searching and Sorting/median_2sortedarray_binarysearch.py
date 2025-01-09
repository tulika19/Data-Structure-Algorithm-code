class Solution:
    def median_twoSortedarray_usingBinarysearch(self, nums1, nums2):
        x = len(nums1)
        y = len(nums2)
        
        # Ensure nums1 is the smaller array
        if x > y:
            nums1, nums2 = nums2, nums1
            x, y = y, x
        
        low, high = 0, x
        combine_length = x + y
        
        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (combine_length + 1) // 2 - partitionX

            # Find max and min values around the partitions
            maxX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minX = float('inf') if partitionX == x else nums1[partitionX]
            
            maxY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minY = float('inf') if partitionY == y else nums2[partitionY]
            
            # Check if partitions are correct
            if maxX <= minY and maxY <= minX:
                # If the combined length is even
                if combine_length % 2 == 0:
                    return (max(maxX, maxY) + min(minX, minY)) / 2.0
                else:
                    # If the combined length is odd
                    return max(maxX, maxY)
            elif maxX > minY:
                # Move the partition left
                high = partitionX - 1
            else:
                # Move the partition right
                low = partitionX + 1

# Example Usage
solution = Solution()
num1 = [1, 2]; num2 = [3, 4]
print(solution.median_twoSortedarray_usingBinarysearch(num1, num2))  # Output: 2.5
