def is_paired(input_string: str) -> bool:
    """ verify that any and all pairs of brackets are matched and nested correctly. """

    brackets_dict = {
        "(": ")",
        "[": "]",
        "{": "}"
    }

    # clean up numbers, letters, etc.
    brackets_list = []
    for char in input_string:
        if char in brackets_dict.keys() or char in brackets_dict.values():
            brackets_list.append(char)
    cleaned_up = ''.join(brackets_list)

    # basic conditions check:
    if len(cleaned_up) == 0:
        return True
    elif len(cleaned_up) % 2 != 0:
        return False
    elif cleaned_up[0] in brackets_dict.values():
        return False
    elif len(cleaned_up) == 2:
        return cleaned_up[1] == brackets_dict[cleaned_up[0]]

    # continuing ...
    stack_list = []

    for char in input_string:
        if char in brackets_dict.keys():
            stack_list.append(char)
        elif char in brackets_dict.values() and char != brackets_dict[stack_list[-1]]:
            return False
        elif char in brackets_dict.values() and char == brackets_dict[stack_list[-1]]:
            stack_list.pop()
            continue

    return len(stack_list) == 0


print(is_paired("}{"))
