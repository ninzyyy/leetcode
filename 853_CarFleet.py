def carFleet(target: int, position: list[int], speed: list[int]) -> int:

    fleet, prev = 0, 0

    # Go through cars in order of their position (lead cars first)
    for p, s in sorted(zip(position, speed))[::-1]:

        # Calculate the time of arrival for each car
        t = (target - p) / s

        # If the last car arrives earlier, it joins the fleet
        if prev < t:
            fleet += 1
            prev = t

    return fleet


print(carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))  # 3
print(carFleet(10, [6, 8], [3, 2]))  # 2
print(carFleet(10, [0, 4, 2], [2, 1, 3]))  # 1
