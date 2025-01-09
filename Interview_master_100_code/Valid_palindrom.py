def valid_palindrom(s):
    # Clean the string by removing non-alphanumeric characters and converting to lowercase
    clean_s = ''.join(char.lower() for char in s if char.isalnum())
    # Reverse the cleaned string
    s_reverse = clean_s[::-1]
    # Check if the cleaned string is equal to its reverse
    if clean_s == s_reverse:
        return "String is a palindrome"
    else:
        return "String is not a palindrome"


# Test cases
s1 = "A man, a plan, a canal: Panama"
s2 = "madam"
s3 = "hello"

# Outputs
print(valid_palindrom(s1))  # Output: "String is a palindrome"
print(valid_palindrom(s2))  # Output: "String is a palindrome"
print(valid_palindrom(s3))  # Output: "String is not a palindrome"
