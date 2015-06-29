__author__ = 'brianhoehne'

test_cases = ["how are you, abc",
              "hello world, def"]

for test in test_cases:
    case = test
    comma = case.find(",")
    phrase = case[:comma]
    remove_chars = list(case[comma + 2:])
    for r in remove_chars:
        phrase = phrase.replace(r,"")

    print(phrase)
