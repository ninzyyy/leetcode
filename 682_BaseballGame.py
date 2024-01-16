
def calPoints(self, operations: list[str]) -> int:

    score = []
    for i in operations:
        if i == 'C':
            score.pop()
        elif i == 'D':
            score.append(2*score[-1])
        elif i == '+':
            score.append(score[-1]+score[-2])
        else:
            score.append(int(i)) # The numbers are of type str

    return sum(score)