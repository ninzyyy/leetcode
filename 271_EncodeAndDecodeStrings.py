
def encode(strs):

    # Adds len(string) + delimiter (!) to the beginning of each string in the list and converts the list to a single string.
    encoded_strs = "".join([str(len(string)) + "!" + string for string in strs])

    return encoded_strs

print(encode(['hello', 'world']))
