__author__ = 'brianhoehne'


test_cases = [
    "zero;two;five;seven;eight;four",
    "three;seven;eight;nine;two"
]

def word_to_digit(word_string, starting_index):
    """

    :param word_string: Full string of spelled out number words
    :param starting_index: Index of string to convert
    :return: String numeric digit
    """
    #print(starting_index)

    if word_string[starting_index] == 'z':
        return "0"
    elif word_string[starting_index] == 'o':
        return "1"
    elif word_string[starting_index] == 't':
        if word_string[starting_index + 1] == "w":
            return "2"
        return "3"
    elif word_string[starting_index] == 'f':
        if word_string[starting_index + 1] == "o":
            return "4"
        return "5"
    elif word_string[starting_index] == 's':
        if word_string[starting_index + 1] == 'i':
            return "6"
        return "7"
    elif word_string[starting_index] == 'e':
        return "8"
    elif word_string[starting_index] == 'n':
        return "9"
    else:
        return "word_to_digit error"


for t in test_cases:
    word_index = 0
    ans = ""
    while True:

        # concatenate ans string
        ans += word_to_digit(t, word_index)

        # increment the word_index to the char after the next ';'
        word_index = t.find(";", word_index + 1) + 1

        # if there isn't a next ';'
        if word_index == 0:
            break

    print(ans)