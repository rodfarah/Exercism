def transpose(*lines: str) -> str:
    """Transpose a string input."""
    lines = "\n".join(lines)
    splited_lines = lines.split("\n")
    max_len = max([len(x) for x in splited_lines])

    # Insert None(s) and create equal length list
    equal_len = []
    for line in splited_lines:
        if len(line) < max_len:
            each_line = [char for char in line]
            for n in range(max_len - len(line)):
                each_line.append(None)
            equal_len.append(each_line)
        else:
            equal_len.append([char for char in line])
    
    # Create a list with characters combined by same indexes
    idx = 0
    combined_list = []
    while idx < max_len:
        each_comb = []
        for lst in equal_len:
            each_comb.append(lst[idx])
        combined_list.append(each_comb)
        idx += 1
    
    # Delete None if situated in the end
    no_last_none = []
    for comb in combined_list:
        while comb and comb[-1] == None:
            comb.pop()
        no_last_none.append(comb)
    
    # Convert residual None's into blank spaces
    none_to_space = []
    for comb in no_last_none:
        comb = [" " if char is None else char for char in comb]
        none_to_space.append(comb)
    joined = ["".join(lst) for lst in none_to_space]
    return "\n".join(joined)
