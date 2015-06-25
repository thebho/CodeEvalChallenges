__author__ = 'brianhoehne'
## Challenge print 2nd to last word from an input string

test_cases = [
    "some line with text",
    "another line"
    ]

for t in test_cases:

    case = t

    #find last space char
    last_space = case.rfind(" ")

    #find second two last space car
    second_to_last = case.rfind(" ", 0, last_space)


    print(case[second_to_last + 1:last_space])