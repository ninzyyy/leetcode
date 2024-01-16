
def twoSum(numbers, target):

    new_numbers = [x - target for x in numbers]

    for i in range(len(new_numbers)):
        if new_numbers[i] in numbers:
            return [numbers[i], numbers.index(new_numbers[i])+1]

    return new_numbers



numbers = [2, 7, 11, 15]
target = 9
print(twoSum(numbers, target))
