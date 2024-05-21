def dailyTemperatures(temperatures):

    res = [0] * len(temperatures)  # Create a zeroes array to "fill"
    stack = []

    for i in range(len(temperatures)):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            j = stack.pop()
            res[j] = i - j
        stack.append(i)
    return res


print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))  # [1,1,4,2,1,1,0,0]
print(dailyTemperatures([20, 40, 60]))  # [1, 1, 0]
