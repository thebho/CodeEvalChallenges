__author__ = 'brianhoehne'

ALPHA_DICT = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0,
              "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0,
              "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0,
              "y": 0, "z": 0}
"""
test inputs
ABbCcc
Good luck in the Facebook Hacker Cup this year!
Ignore punctuation, please :)
Sometimes test cases are hard to make up.
So I just go consult Professor Dalves
"""



##### MAIN THREAD #####

# read inputs
# convert to lowerCase
# copy ALPHA_DICT locally
# iterate over string
# convert dict to sorted list by key not equal to 0
# iterate over sorted list, 26*[0] + 25*[1]
# print sum