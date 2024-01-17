def evalRPN(self, tokens: list[str]) -> int:

    stack = []
    while tokens:
        stack.append(tokens.pop(0))

        if stack[-1] == '+':
            val = int(stack[-3]) + int(stack[-2])
            stack = stack[:-3]
            stack.append(str(val))

        if stack[-1] == '-':
            val = int(stack[-3]) - int(stack[-2])
            stack = stack[:-3]
            stack.append(str(val))

        if stack[-1] == '*':
            val = int(stack[-3]) * int(stack[-2])
            stack = stack[:-3]
            stack.append(str(val))

        if stack[-1] == '/':
            val = int(float(stack[-3]) / float(stack[-2]))
            stack = stack[:-3]
            stack.append(str(val))

    return int(stack[0])