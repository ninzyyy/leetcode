
def characterReplacement(s: str, k: int) -> int:

    left = 0
    longest = 0
    d = {}

    for right in range(len(s)):
        d[s[right]] = 1 + d.get(s[right], 0)

        while (right - left + 1) - max(d.values()) > k:
            d[s[left]] -= 1
            left += 1
        longest = max(longest, (right - left + 1))

    return longest

print(characterReplacement('ABAB', 2))
# Output should be 4