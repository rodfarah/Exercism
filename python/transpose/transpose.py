def transpose(*lines: str) -> str:
    """Transpose a string input."""
    lines = "\n".join(lines)
    print(lines, "\n")
    splited_lines = lines.split("\n")
    print(splited_lines, "\n")
    max_lenght = max([len(line) for line in splited_lines])

    # fill out any symbol (~) to end of lines in order to keep them with the same lenght
    equal_length = [line + (max_lenght - len(line)) * "~" for line in splited_lines]
    print(equal_length, "\n")

    # create a list with transposed lines
    transposed_list = []
    for n in range(0, max_lenght):
        each_one = []
        for line in equal_length:
            each_one.append(line[n])
        transposed_list.append("".join(each_one))
    print(transposed_list, "\n")

    # remove symbol (~) from end of lines, keeping eventual original blank spaces at the end of lines
    for n in range(len(transposed_list)):
        while True:
            if not transposed_list[n].endswith("~"):
                break
            else:
                transposed_list[n] = transposed_list[n].removesuffix("~")
                

    # if there is a symbol (~) in the middle of a line, convert it into a blank space
    result = [line.replace("~", " ") for line in transposed_list]
    return "\n".join(result)


print(transpose("ABCDEF", "1234"))