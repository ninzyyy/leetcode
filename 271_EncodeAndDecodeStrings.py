def encode(strs):
    string = ""
    for s in strs:
        # Add complex delimiter -> length of string + $
        # ["i","love","you"] -> "1$i4$love3$you"
        string += str(len(s)) + "$" + s
    return string


def decode(string):

    decoded_str, i = [], 0

    while i < len(string):
        j = i
        while string[j] != "$":
            j += 1

        # Get length of word before delimiter
        length = int(string[i:j])

        # Get the word
        word = string[j + 1 : j + 1 + length]

        decoded_str.append(word)
        i = j + 1 + length

    return decoded_str


print(decode(encode(["i", "love", "you"])))
print(decode(encode(["i", "love", "$"])))
print(decode(encode(["$i", "lo$ve", "$you", "too$"])))
