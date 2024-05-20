def generateParenthesis(n: int) -> list[str]:

    res = []

    def backtrack(curr, opened, closed):

        if opened == closed == n:
            res.append(curr)
            return

        if n > opened:
            backtrack(curr + "(", opened + 1, closed)
            # Once the call stack of backtracks is done, the executor will move to the next "if" statement below

        if opened > closed:
            backtrack(curr + ")", opened, closed + 1)

    backtrack("", 0, 0)
    return res


print(generateParenthesis(3))  # ['((()))', '(()())', '(())()', '()(())', '()()()']
print(generateParenthesis(1))  # ['()']
