def isAnagram(s: str, t: str) -> bool:

    if len(s) != len(t):
        return False

    for letter in set(s):
        if s.count(letter) != t.count(letter):
            return False

    return True


print(isAnagram("anagram", "nagaram"))  # True
print(isAnagram("rat", "car"))  # False
