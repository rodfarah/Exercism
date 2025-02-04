def group_converter(group:list[str]) -> str:
    """ 
    Convert a group of OCR lines into a string of numbers.
    A group consists of four lines representing numbers in a 3x4 grid format. Each number is
    represented by a 3x3 grid of characters, with the fourth line being whitespace.
    Args:
        group (list[str]): A list of strings where each string represents a line in the OCR format.
                           Must contain a multiple of 4 lines, where each line has equal length
                           and the length is a multiple of 3.
    Returns:
        str: A string containing the decoded numbers, followed by a comma.
             Unknown patterns are represented by '?'.
    Raises:
        ValueError: If the number of input lines is not a multiple of four
        ValueError: If the number of input columns is not a multiple of three
        ValueError: If any fourth line in the group contains non-whitespace characters
    Example:
        >>> group = [
        ...     " _  _ ",
        ...     "| | _|",
        ...     "|_||_ ",
        ...     "      "
        ... ]
        >>> group_converter(group)
        "23,"
    """


    # validate all lines have equal lengths and are multiple of 3
    # set contains only one element (line lenght) as repeated values are excluded
    chars_in_lines_set= set(len(line) for line in group)
    value_in_set = next(iter(chars_in_lines_set))
    if len(chars_in_lines_set) != 1 or value_in_set%3 != 0:
        raise ValueError("Number of input columns is not a multiple of three")
    
    # a group is a set of four lines
    num_of_numbers_per_group = int(value_in_set/3)

    three_by_three_all_lines = []
    for line in group:
        idx = 0
        while idx <= value_in_set-1:
            three_by_three_all_lines.append(line[idx:idx+3])
            idx += 3
    
    each_number = []

    idx = 0
    for _ in range(num_of_numbers_per_group):
        each_number.append(three_by_three_all_lines[idx::num_of_numbers_per_group])
        idx += 1
    
    # Define possibilities (keys are possible numbers, values are chars representations)
    dict_of_numbers = {
        "1": ("   ", "  |", "  |"),
        "2": (" _ ", " _|", "|_ "),
        "3": (" _ ", " _|", " _|"),
        "4": ("   ", "|_|", "  |"),
        "5": (" _ ", "|_ ", " _|"),
        "6": (" _ ", "|_ ", "|_|"),
        "7": (" _ ", "  |", "  |"),
        "8": (" _ ", "|_|", "|_|"),
        "9": (" _ ", "|_|", " _|"),
        "0": (" _ ", "| |", "|_|"),
    }
    
    result = []
    for number in each_number:
        # verify if last line is only whitespaces
        if not number[-1].isspace():
            raise ValueError("Every line multipĺe of 4 must be composed only by whitespaces")
        number.pop()
        # verify results:
        found_match = False
        for k, v in dict_of_numbers.items():
            if v == tuple(number):
                result.append(k)
                found_match = True
                break
        if not found_match:
            result.append("?")
    return "".join(result)


def convert(input_grid:list[str]) -> str:
    """Convert a grid representation of numbers to their string representation.
    This function takes a grid of characters representing one or more numbers and converts them
    to their corresponding decimal representation. Each number in the grid is represented by
    4 lines of characters, where each digit takes up 3 columns.
    Args:
        input_grid (list[str]): A list of strings representing the grid of numbers.
            Each number must be 4 lines high and each digit must be 3 columns wide.
    Returns:
        str: A string containing the decimal representation of the numbers,
            with multiple numbers separated by commas.
    Raises:
        ValueError: If the number of input lines is not a multiple of four.
    Example:
        >>> grid = [
        ...     " _ ",
        ...     "| |",
        ...     "|_|",
        ...     "   "
        ... ]
        >>> convert(grid)
        '0'
    """

    # verify 'four lines per group' condition
    if len(input_grid)%4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    
    final_result = []
    line_idx = 0
    for _ in range(int(len(input_grid)/4)):
        final_result.append(group_converter(input_grid[line_idx:line_idx+4]))
        line_idx+=4

    return ",".join(final_result)

