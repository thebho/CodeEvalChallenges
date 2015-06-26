__author__ = 'brianhoehne'

test_cases = [
    "osSE5Gu0Vi8WRq93UvkYZCjaOKeNJfTyH6tzDQbxFm4M1ndXIPh27wBA rLclpg|"
    " 3 35 27 62 51 27 46 57 26 10 46 63 57 45 15 43 53",

    "3Kucdq9bfCEgZGF2nwx8UpzQJyHiOm0hoaYP6ST1WM7Nks5XjrR4IltBeDLV vA|"
    " 2 26 33 55 34 50 33 61 44 28 46 32 28 30 3 50 34 61 40 7 1 31"
]


def convert_input_to_ans_tuple(string: str):
    """
    Finds pipe and returns a tuple of answer string and list of int indexes
    :param string: input string with coded chars and a space separated string of ints
    :return: (str,[int])
    """

    pipe_index = string.find("|")

    # check for missing pipe char
    if pipe_index > 0:

        #split string
        return_string = string[:pipe_index]

        # convert
        return_list = list(map(int,string[pipe_index + 2:].split()))
        return (return_string, return_list)

    else:
        print("Pipe Error")
        return None, None


def crack_code(string: str, indexes: [int]):

    # initialize return string
    return_string = ""

    # for each index concatenate return_string with index from string
    for i in indexes:
        return_string += string[i - 1]

    return return_string

for i in range(len(test_cases)):

    case = test_cases[i]

    # separate string from ints using find("|") convert to (ans_string,[ans_indexes])
    ans_string, ans_indexes = convert_input_to_ans_tuple(case)
    #print(len(ans_string))

    # iterate over list of ints to find answer
    print(crack_code(ans_string,ans_indexes))