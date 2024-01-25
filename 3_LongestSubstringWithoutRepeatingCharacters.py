
def lengthOfLongestSubstring(s: str) -> int:

        chars = set()
        left = 0
        result = 0

        for right in range(len(s)):
            print(s[left:right], chars)

            if s[right] in chars:
                chars.remove(s[left])
                left += 1

            chars.add(s[right])

            result = max(result, right - left + 1)
        return result

print(lengthOfLongestSubstring("pwwkew"))
# Output should be 3