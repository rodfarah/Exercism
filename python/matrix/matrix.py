def format_rows(matrix: str) -> list:
    """Given one string with break lines, this function return 
    a list with lists of strings. Eg. [["1", "2"], ["3", "4"]]
    """
    try:
        no_new_lines = matrix.split("\n")
        est = []
        for string in no_new_lines:
            est.append(string.split(" "))
        return est

    except:
        return matrix


class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def row(self, index: int) -> list:
        """Return a matrix object's row, given an index as parameter"""
        formated_rows = format_rows(self.matrix_string)
        return [int(str_num) for str_num in formated_rows[index - 1]]

    def column(self, index: int) -> list:
        """Return a matrix object's column, given an index as parameter"""
        formated_rows = format_rows(self.matrix_string)
        result = []
        for n in range(len(formated_rows)):
            result.append(int(formated_rows[n][index - 1]))
        return result
