__author__ = 'brianhoehne'

COL, ROW = "Col","Row"

TEST_CASES = [
    "SetCol 32 20",
    "SetRow 15 7",
    "SetRow 16 31",
    "QueryCol 32",
    "SetCol 2 14",
    "QueryRow 10",
    "SetCol 14 0",
    "QueryRow 15",
    "SetRow 10 1",
    "QueryCol 2"
]

class Matrix:

    def __init__(self, size: int):
        self.matrix = []

        # create matrix
        for i in range(size):
            self.matrix.append([0 for x in range(size)])

    def set_col(self, index: int, value: int):
        for m in self.matrix:
            m[index] = value

    def set_row(self, index: int, value: int):
        for i in range(len(self.matrix[index])):
            self.matrix[index][i] = value

    def query_col(self, index: int):
        col_sum = 0
        for m in self.matrix:
            col_sum += m[index]
        print(col_sum)

    def query_row(self, index: int):
        print(sum(self.matrix[index]))

    def set_function(self, set_string: str):
        """
        Converts a input string into a set index and value and executes
        appropriate row/col method
        :param set_string:
        """

        # find starting index for matrix_index and new_value
        set_index = set_string.find(" ") + 1
        value_index = set_string.find(" ",set_index) + 1

        # slice set_string to find the input index and value
        matrix_index = int(set_string[set_index:value_index - 1])
        new_value = int(set_string[value_index:])

        # switch over type of set command
        if set_string.find("SetCol") == 0:
            self.set_col(matrix_index,new_value)
        elif set_string.find("SetRow") == 0:
            self.set_row(matrix_index,new_value)
        else:
            print("set_function string error")

    def query_function(self, query_string: str):
        """
        Converts a input string into a query index and executes
        appropriate row/col method
        :param query_string: input "QueryExample 10"
        """

        # finds the index of the first space + 1
        query_index = query_string.find(" ") + 1

        # slices query_string at index into int value from string
        matrix_index = int(query_string[query_index:])

        # switch over type of query command
        if query_string.find("QueryCol") == 0:
            self.query_col(matrix_index)
        elif query_string.find("QueryRow") == 0:
            self.query_row(matrix_index)
        else:
            print("set_function string error")

# initial matrix
matrix = Matrix(256)

for t in TEST_CASES:

    # read case input
    case = t

    # check first char for S or Q

    # if S execute set_function, with arguments (matrix,command)
    if case[0] == 'S':
        matrix.set_function(case)

    # if Q execute print_query, with arguments (matrix,command)
    elif case[0] == 'Q':
        matrix.query_function(case)

    else:
        print("input read error")