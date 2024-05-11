def longestConsecutive(nums: list[int]) -> int:

    numsSet = set(nums)
    longest = 0

    for n in numsSet:

        # Is it a start of a sequence?
        if (n - 1) not in numsSet:

            # Check if number after exists in set
            length = 1
            while (n + length) in numsSet:
                length += 1

            # Update longest sequence
            longest = max(length, longest)

    return longest


print(longestConsecutive([100, 4, 200, 1, 3, 2]))  # 4
print(longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 9
print(longestConsecutive([1, 2, 0, 1, 2, 3]))  # 4
