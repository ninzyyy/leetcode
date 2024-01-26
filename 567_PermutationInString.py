
def checkInclusion(s1: str, s2: str) -> bool:

    if len(s1) > len(s2):
        return False

    left = 0
    right = len(s1) - 1
    d1 = {}
    for x in s1:
        d1[x] = 1 + d1.get(x, 0)

    while right < len(s2):
        d2 ={}
        for y in s2[left:right + 1]:
            d2[y] = 1 + d2.get(y, 0)

        if d1 == d2:
            return True
        left += 1
        right += 1

    return False


checkInclusion('abc', 'baxyzbac')