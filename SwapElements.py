__author__ = 'brianhoehne'

test_cases = [
    "1 2 3 4 5 6 7 8 9 : 0-8",
    "1 2 3 4 5 6 7 8 9 10 : 0-1, 1-3"
]
for test in test_cases:
    T = test
    colon = T.find(":")
    num_list = list(T[:colon].split())
    swap_list = []
    current_swap_start = colon + 1
    for i in range(colon + 1, len(T)):
        if T[i] == "," or i == len(T) - 1:
            swap_local = None;
            if T[i] == ",":
                swap_local = T[current_swap_start:i]
            else:
                swap_local = T[current_swap_start:i+1]
            swap_local = swap_local.replace("-"," ")
            low,high = list(map(int,swap_local.split()))
            temp = num_list[low]
            num_list[low] = num_list[high]
            num_list[high] = temp
            current_swap_start = i + 1
    print(" ".join(n for n in num_list))
