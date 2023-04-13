def transpose(*lines: str) -> str:
    """Transpose a string input."""
    lines = "\n".join(lines)
    splited_lines = lines.split("\n")
    max_lenght = max([len(line) for line in splited_lines])

    # fill out any symbol (~) to end of lines in order to keep them with the same lenght
    equal_length = []
    for line in splited_lines:
        equal_length.append(line + (max_lenght - len(line)) * "~")

    # create a list with transposed lines
    each_one = []
    transposed_list = []
    for n in range(0, max_lenght):
        for line in equal_length:
            each_one.append(line[n])
        transposed_list.append("".join(each_one))
        each_one = []

    # remove symbol (~) from end of lines, keeping eventual original blank spaces at the end of lines
    for n in range(len(transposed_list)):
        while True:
            if not transposed_list[n].endswith("~"):
                break
            else:
                transposed_list[n] = transposed_list[n].removesuffix("~")
                continue

    # if in the middle of a line, convert symbol (~) into a blank space
    result = [line.replace("~", " ") for line in transposed_list]
    return "\n".join(result)
