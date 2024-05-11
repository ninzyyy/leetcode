def isPalindrome(s: str) -> bool:

    # Remove non-alphanumeric chars and convert to lower case
    s = "".join([x for x in s if x.isalnum()]).lower()

    # Initialize pointers
    left, right = 0, len(s) - 1

    while left < right:
        if not s[left] == s[right]:
            return False
        left += 1
        right -= 1
    return True


print(isPalindrome("ra#ce&car"))  # True
print(isPalindrome("A man, a plan, a canal: Panama"))  # True
print(isPalindrome("Hello world!"))  # False
