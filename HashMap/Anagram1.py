#Q: Find all anagrams of a string in another string.

class Solution: 
    def FindAnagram(self, p, s):
        # If the length of p is greater than s, no anagrams are possible
        if len(p) > len(s):
            return []

        # Initialize frequency counts for p and the first window of s
        pCount, sCount = {}, {}
        res = []

        # Populate the frequency counts for p and the first window of s
        for i in range(len(p)):
            pCount[p[i]] = 1 + pCount.get(p[i], 0)
            sCount[s[i]] = 1 + sCount.get(s[i], 0)

        # Check if the first window is an anagram
        if pCount == sCount:
            res.append(0)

        # Sliding window logic
        l = 0  # Initialize the left pointer
        for r in range(len(p), len(s)):
            # Add the new character at the right pointer to sCount
            sCount[s[r]] = 1 + sCount.get(s[r], 0)
            # Remove the character at the left pointer from sCount
            sCount[s[l]] -= 1
            if sCount[s[l]] == 0:  # Remove the character from the dictionary if its count is 0
                sCount.pop(s[l])
            l += 1  # Move the left pointer

            # Check if the current window matches pCount
            if sCount == pCount:
                res.append(l)

        return res


# Instantiate the solution class
solution = Solution()

# Test cases
test_cases = [
    # Regular cases
    {"s": "cbaebabacd", "p": "abc", "expected": [0, 6]},  # Anagrams at indices 0 and 6
    {"s": "abab", "p": "ab", "expected": [0, 1, 2]},     # Overlapping anagrams

    # Edge cases
    {"s": "", "p": "", "expected": []},                  # Both strings empty
    {"s": "abc", "p": "", "expected": []},               # Empty `p`, non-empty `s`
    {"s": "", "p": "abc", "expected": []},               # Empty `s`, non-empty `p`
    {"s": "a", "p": "abc", "expected": []},              # `p` longer than `s`

    # Case with no anagrams
    {"s": "abcdefg", "p": "hij", "expected": []},        # No anagrams

    # Case with all characters matching
    {"s": "aaabbbccc", "p": "abc", "expected": [0, 1, 2, 3, 4, 5, 6]},  # Many overlapping matches

    # Case with repeating characters
    {"s": "aaaaaa", "p": "aa", "expected": [0, 1, 2, 3, 4]},            # Sliding window with repeating chars
]

# Run all test cases
for i, case in enumerate(test_cases):
    result = solution.FindAnagram(case["p"], case["s"])
    print(f"Test case {i + 1}: s = \"{case['s']}\", p = \"{case['p']}\"")
    print(f"Expected: {case['expected']}, Got: {result}")
    print("Pass" if result == case["expected"] else "Fail")
    print("-" * 40)
