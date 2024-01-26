from collections import Counter

def checkInclusion(s1: str, s2: str) -> bool:

    if len(s1) > len(s2):
        return False

    # Initialize pointers and s1 dict
    left = 0
    right = len(s1) - 1
    d1 = Counter(s1)

    while right < len(s2):

        # Create window dict
        d2 = Counter(s2[left:right+1])

        # If s1 dict and window match then True
        if d1 == d2:
            return True

        # Shift window to the right
        left += 1
        right += 1

    return False


checkInclusion('abc', 'baxyzbac')