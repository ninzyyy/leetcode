def evalRPN(tokens: list[str]) -> int:

    stack = []

    for t in tokens:

        if t not in "+-*/":
            stack.append(int(t))

        else:
            num = stack.pop()
            if t == "+":
                stack[-1] += num
            elif t == "-":
                stack[-1] -= num
            elif t == "*":
                stack[-1] *= num
            else:
                stack[-1] = int(stack[-1] / num)

    return stack[0]


print(evalRPN(["2", "1", "+", "3", "*"]))  # 9
print(evalRPN(["4", "13", "5", "/", "+"]))  # 6
