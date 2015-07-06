__author__ = 'brianhoehne'

test_course = ["#########_##",
               "########C_##",
               "#######_####",
               "######_#C###",
               "#######_C###",
               "#######_####",
               "######C#_###",
               "######C_####",
               "#######_####",
               "#######_####"]

current = None
previous = None
for i in range(len(test_course)):
    current_C = test_course[i].find("C")
    if current_C > -1:
        current = current_C
        if previous == None or current == previous:
            test_course[i] = test_course[i].replace("C","|",1)
        elif previous > current:
            test_course[i] = test_course[i].replace("C","/",1)
        elif previous < current:
            test_course[i] = test_course[i].replace("C","\\",1)
    else:
        current = test_course[i].find("_")
        if previous == None or current == previous:
            test_course[i] = test_course[i].replace("_","|",1)
        elif previous > current:
            test_course[i] = test_course[i].replace("_","/",1)
        elif previous < current:
            test_course[i] = test_course[i].replace("_","\\",1)
    print(test_course[i])
    previous = current

