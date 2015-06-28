__author__ = 'brianhoehne'

import math

test_cases = [
    "(25, 4) (1, -6)",
    "(47, 43) (-25, -11)"
]

def convert_input(string:str):

    stripped_string = string.replace("(","")
    stripped_string = stripped_string.replace(")","")
    stripped_string = stripped_string.replace(",","")
    stripped_string = list(map(int,stripped_string.split()))
    print(stripped_string)
    return stripped_string

def calculate_distance(x1,y1,x2,y2):
    a = (x1 - x2) ** 2
    b = (y1 - y2) ** 2
    return int(math.sqrt(a+b))

for t in test_cases:

    # strip parentheses and commas
    x1,y1,x2,y2 = convert_input(t)

    # call a function converts points to distance
    print(calculate_distance(x1,y1,x2,y2))