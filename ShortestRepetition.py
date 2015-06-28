__author__ = 'brianhoehne'

test_cases = ["abcabcabcabc",
              "bcbcbcbcbcbcacbcbcbcbcbcbcbc",
              "dddddddddddddddddddd",
              "adcdefg"]


def check_repetition(string: str, index):
    str_len = len(string)
    if check_index == str_len - 1:
        return str_len
    elif check_index == 0:
        return 1
    else:
        check = ""
        while len(check) < str_len:
            check += string[:check_index + 1]

        if check == string:
            return check_index + 1
        else:
            return -1

for t in test_cases:
    case = t

    check_index = case.find(case[-1])


    # base case
    if check_index == len(case) - 1:
        print(len(case))
    elif check_index == 0:
        print(1)
    else:
        while True:
            if check_index == 0:
                print(len(case))
                break
            elif case[check_index] != case[-1]:
                check_index -= 1
                continue
            else:
                check_rep = check_repetition(case, check_index)
                if check_rep >= 0:
                    print(check_rep)
                    break
                else:
                    check_index -= 1
