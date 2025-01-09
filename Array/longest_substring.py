def longest_subarray(s):
    l, length = 0, 0  # Initialize left pointer and max length
    seen_char = {}  # Dictionary to track the last seen index of characters

    for r in range(len(s)):  # Iterate through the string
        char = s[r]
        # If the character is already seen and within the current window
        if char in seen_char and seen_char[char] >= l:
            l = seen_char[char] + 1  # Move the left pointer

        # Calculate the current window length and update max length
        length = max(length, r - l + 1)

        # Update the character's last seen index
        seen_char[char] = r

    return length


# Clean the input string to remove commas
s = "abcacbdd"
print(longest_subarray(s))  # Output: 4
