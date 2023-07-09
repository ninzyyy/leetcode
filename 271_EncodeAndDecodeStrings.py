
def encode(strs):
    #Adds len(string) + delimiter (!) to the beginning of each string in the list and converts the list to a single string.

    encoded_strs = "".join([str(len(string)) + "!" + string for string in strs])

    return encoded_strs


def decode(string):
    #Takes the encoded string and decodes it.

    decoded_str = []
    i = 0

    while i < len(string):
        j = i
        while string[j] != '!': #Finds the delimiter.
            j += 1
        length = int(string[i:j]) #Gets the length of the string after the delimiter.
        decoded_str.append(string[j+1 : j+1+length]) #Adds the string to the final list.
        i = j + 1 + length #Sets new "starting" point i

    return decoded_str
