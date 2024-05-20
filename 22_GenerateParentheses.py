def generateParenthesis(n: int) -> list[str]:

    res = []

    def backtrack(curr, opened, closed):

        if opened == closed == n:
            res.append(curr)
            return

        if n > opened:
            backtrack(curr + "(", opened + 1, closed)

        if opened > closed:
            backtrack(curr + ")", opened, closed + 1)

    backtrack("", 0, 0)
    return res


print(generateParenthesis(3))  # ['((()))', '(()())', '(())()', '()(())', '()()()']
print(generateParenthesis(1))  # ['()']
