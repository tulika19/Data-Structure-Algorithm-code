class Solution(object):
    def isAnagram(self, s, t):
        # If lengths are not the same, they can't be anagrams
        if len(s) != len(t):
            return False
        
        # Hash map (dictionary) to count character frequencies in `s`
        count = {}
        
        # Count the occurrences of each character in `s`
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        # Subtract the counts using characters in `t`
        for char in t:
            if char not in count:  # If `t` has an extra character not in `s`
                return False
            count[char] -= 1
            if count[char] < 0:  # If `t` uses a character too many times
                return False
        
        # If all counts are zero, it's an anagram
        return True
solution = Solution()

# Test cases
print(solution.isAnagram("anagram", "nagaram"))  # Output: True
print(solution.isAnagram("rat", "car"))          # Output: False
print(solution.isAnagram("a", "a"))              # Output: True
print(solution.isAnagram("ab", "a"))             # Output: False
print(solution.isAnagram("", ""))                # Output: True
