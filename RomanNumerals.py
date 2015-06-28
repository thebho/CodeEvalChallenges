__author__ = 'brianhoehne'

import sys

test_cases = [
    3158,
    2499,
    2186,
    409,
    1935,
    1297,
    624,
    2691,
    202,
    2530,
    1047,
    2671,
    2756,
    2704,
    127,
    721,
    2930,
    353,
    3850,
    3301,
    876,
    2697,
    560,
    1743,
    2752,
    3946,
    50,
    1527,
    1005,
    3203,
    3557,
    2079,
    1623,
    ]

for t in test_cases:
    case = t

    ans = ""

    # Thousands
    thousands = case // 1000
    for t in range(thousands):
        ans += "M"

    case -= thousands * 1000

    # print(case)

    # Hundreds
    hundreds = case // 100

    if case > 100:
        if hundreds == 9:
            ans += "CM"
        elif hundreds >= 5:
            ans += "D"
            for h in range(hundreds - 5):
                ans += "C"
        elif hundreds == 4:
            ans += "CD"
        else:
            for h in range(hundreds):
                ans += "C"

    case -= hundreds * 100

    # print(case)

    # Tens

    tens = case // 10

    if case > 10:
        if tens == 9:
            ans += "XC"
        elif tens >= 5:
            ans += "L"
            for t in range(tens - 5):
                ans += "X"
        elif tens == 4:
            ans += "XL"
        else:
            for t in range(tens):
                ans += "X"

        case -= tens * 10

    # print(case)

    # Ones

    if case > 0:
        if case == 9:
            ans += "IX"
        elif case >= 5:
            ans += "V"
            for c in range(case - 5):
                ans += "I"
        elif case == 4:
            ans += "IV"
        else:
            for c in range(case):
                ans += "I"

    print(ans)




test_cases.close()