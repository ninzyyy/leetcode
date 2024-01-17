def evalRPN(self, tokens: list[str]) -> int:

    stack = []
    while tokens:
        stack.append(tokens.pop(0))

        if stack[-1] == '+':
            stack.pop()
            first = int(stack.pop())
            second = int(stack.pop())
            stack.append(second + first)

        if stack[-1] == '-':
            stack.pop()
            first = int(stack.pop())
            second = int(stack.pop())
            stack.append(second - first)

        if stack[-1] == '*':
            stack.pop()
            first = int(stack.pop())
            second = int(stack.pop())
            stack.append(second * first)

        if stack[-1] == '/':
            stack.pop()
            first = int(stack.pop())
            second = int(stack.pop())
            stack.append(int(float(second / first)))

    return int(stack[0])