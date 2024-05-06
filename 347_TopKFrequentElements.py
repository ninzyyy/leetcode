def topKFrequent(nums: list[int], k: int) -> list[int]:

    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    # Hash map to count freq of all nums
    for n in nums:
        count[n] = 1 + count.get(n, 0)

    # Bucket Sort (where index is the count)
    for n, c in count.items():
        freq[c].append(n)

    solution = []
    # Go through freq in reverse order (highest freq first)
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            solution.append(n)
            if len(solution) == k:
                return solution


print(topKFrequent([1, 1, 1, 2, 2, 3], 2))  # [1,2]
print(topKFrequent([1], 1))  # [1]
print(topKFrequent([1, 2], 2))  # [1,2]
