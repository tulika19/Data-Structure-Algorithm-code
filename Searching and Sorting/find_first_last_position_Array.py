class Solution(object):
    def searchRange(self, nums, target):
        # Find the leftmost index of the target
        left = self.binsearch(nums, target, True)
        # Find the rightmost index of the target
        right = self.binsearch(nums, target, False)
        # Return the first and last positions
        return [left, right]

    # Helper function to perform binary search
    def binsearch(self, nums, target, leftbias):
        """
        Perform binary search to find the index of the target.
        If leftbias=True, find the leftmost index.
        If leftbias=False, find the rightmost index.
        """
        l, r = 0, len(nums) - 1  # Initialize the search bounds
        i = -1  # Default value if the target is not found
        
        while l <= r:
            m = (l + r) // 2  # Calculate the midpoint
            
            if target < nums[m]:  # If the target is less than nums[m], search the left half
                r = m - 1
            elif target > nums[m]:  # If the target is greater than nums[m], search the right half
                l = m + 1
            else:  # When nums[m] matches the target
                i = m  # Update the potential index
                if leftbias:
                    r = m - 1  # Continue searching in the left half for the leftmost index
                else:
                    l = m + 1  # Continue searching in the right half for the rightmost index
        
        return i  # Return the index of the target (or -1 if not found)
