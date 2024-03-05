import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        solution = ""
        min_word = min(strs)
        num = 0

        for n in range(len(min_word)):
            for word in strs:
                if not word[num] == min_word[num]:
                    return solution
            solution += word[num]
            num += 1

        return solution