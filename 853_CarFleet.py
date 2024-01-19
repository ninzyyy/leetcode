
def carFleet(target: int, position: list[int], speed: list[int]) -> int:

    l = [[pos, spd] for pos, spd in zip(position, speed)]
    stack = []

    for pos, spd in sorted(l)[::-1]: #sorted, reversed
        time = (target - pos) / spd
        stack.append(time)

        # Check to see if the any cars reaches target before or
        # same time as another (and merge as one fleet)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
    return len(stack)

print(carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))