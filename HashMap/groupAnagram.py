# Problem: Group Anagrams
# Plan:
# 1. Create a dictionary to group words by their sorted representation.
# 2. For each word in the input, sort the characters to form a key.
# 3. Group all words with the same key.
# 4. Return the grouped anagrams as a list of lists.

class Solution:
    def groupAnagrams(self, strs):
        # Edge case: empty input
        if not strs:
            return []
        
        # Dictionary to store grouped anagrams
        anagrams = {}

        # Iterate through each word
        for word in strs:
            # Sort the word to create a unique key
            key = "".join(sorted(word))
            # Use the key to group anagrams
            anagrams[key] = anagrams.get(key, []) + [word]

        # Return the grouped anagrams
        return list(anagrams.values())
Solution = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(Solution.groupAnagrams(strs))

# Example:
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    
