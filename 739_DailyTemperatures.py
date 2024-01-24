
def dailyTemperatures(temperatures):
    answer = [0] * len(temperatures) # Create a zeroes array to "fill"
    stack = []

    for index, temp in enumerate(temperatures):
        while stack and temp > stack[-1][1]:
            stack_i, stack_t = stack.pop()
            answer[stack_i] = index - stack_i
        stack.append([index, temp])
        print(answer)
    return answer

print(dailyTemperatures([73,74,75,71,69,72,76,73]))
