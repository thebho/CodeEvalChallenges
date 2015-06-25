__author__ = 'brianhoehne'

ALPHA_DICT = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0,
              "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0,
              "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0,
              "y": 0, "z": 0}
INPUTS = [
    "ABbCcc",
    "Good luck in the Facebook Hacker Cup this year!",
    "Ignore punctuation, please :)",
    "Sometimes test cases are hard to make up.",
    "So I just go consult Professor Dalves"
]



##### MAIN THREAD #####

# read inputs
for i in INPUTS:

    # convert to lowerCase
    input_lower = i.lower()

    # copy ALPHA_DICT locally
    local_dict = ALPHA_DICT.copy()

    # iterate over string
    for i_l in input_lower:

        # increment dictionary value if i_l is a valid dictionary key
        if i_l in local_dict:
            local_dict[i_l] += 1

    # convert dict to sorted list by key not equal to 0
    local_key_list = sorted(local_dict.keys(), key = lambda d: local_dict[d], reverse=True)

    ans = 0
    current_beautiful_value = 26

    # iterate over sorted list, 26*[0] + 25*[1]
    for l_k_l in local_key_list:

        # base case if
        if local_dict[l_k_l] == 0:
            break

        # increment ans
        ans += local_dict[l_k_l] * current_beautiful_value

        # decrement current_beautiful_value
        current_beautiful_value -= 1

    # print sum
    print(ans)