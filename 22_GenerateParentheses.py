def generateParenthesis(n: int) -> list[str]:

    solution = []

    def backtrack(current, openBrackets, closedBrackets):

        # Base Case
        if openBrackets == closedBrackets == n:
            solution.append("".join(current))
            return

        if closedBrackets < openBrackets:
            current.append(")")
            backtrack(current, openBrackets, closedBrackets + 1)
            current.pop()

        if openBrackets < n:
            current.append("(")
            backtrack(current, openBrackets + 1, closedBrackets)
            current.pop()

    backtrack(["("], 1, 0)
    return solution

print(generateParenthesis(3))