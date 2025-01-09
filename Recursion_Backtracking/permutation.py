class Solution(object):
    def permute(self, nums):
        """
        Generates all permutations of the input list nums.
        
        Args:
            nums (List[int]): A list of integers.
        
        Returns:
            List[List[int]]: A list containing all permutations of nums.
        """
        result = []  # To store all permutations
        
        def backtrack(current, remaining):
            """
            Helper function to perform backtracking.
            
            Args:
                current (List[int]): The current permutation being constructed.
                remaining (List[int]): The numbers yet to be added to the permutation.
            """
            # Base case: if no numbers remain, add the current permutation to the result
            if not remaining:
                result.append(current[:])  # Append a copy of the current permutation
                return
            
            # Iterate through the remaining numbers
            for i in range(len(remaining)):
                # Choose the next number and create a new state
                new_current = current + [remaining[i]]  # Add the chosen number
                new_remaining = remaining[:i] + remaining[i+1:]  # Exclude the chosen number
                
                # Recursively backtrack with the updated state
                backtrack(new_current, new_remaining)
        
        # Start the backtracking process
        backtrack([], nums)
        return result
# Instantiate the solution
sol = Solution()

# Input list
nums = [1, 2, 3]

# Generate permutations
output = sol.permute(nums)

# Print the output
print(output)
# Test cases
test_cases = [
    ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
    ([0], [[0]]),
    ([1, 2], [[1, 2], [2, 1]]),
    ([], [[]]),
]

# Run and validate test cases
sol = Solution()
for i, (input_data, expected) in enumerate(test_cases):
    output = sol.permute(input_data)
    print(f"Test Case {i+1}: {'Pass' if sorted(output) == sorted(expected) else 'Fail'}")
