
def encode(strs):

    strs = [str(len(string)) + "!" + string for string in strs]
    strs = "".join(strs)

    return strs

print(encode(['hello', 'world']))
