"""Write a function to convert from normal numbers to Roman Numerals."""


def num_to_letters(str_number: str, str_list: list[str]) -> str:
    """Receive a string number and return a Roman Numeral"""
    first_group = [1, 2, 3]
    second_group = [6, 7, 8]

    number = int(str_number)

    if number in first_group:
        return number * str_list[0]
    elif number == 4:
        return str_list[0] + str_list[1]
    elif number == 5:
        return str_list[1]
    elif number in second_group:
        return str_list[1] + (second_group.index(number) + 1) * str_list[0]
    elif number == 9:
        return str_list[0] + str_list[2]
    return ""


FIRST_GROUP = ["I", "V", "X"]
SECOND_GROUP = ["X", "L", "C"]
THIRD_GROUP = ["C", "D", "M"]


def roman(number: int) -> str:
    """Receive an int from 1 to 3999 and return Roman Numerals"""
    str_dict = {k: v for k, v in enumerate(
        reversed([str_num for str_num in str(number)]), 1)}

    result = []
    for k, v in str_dict.items():
        if k == 1:
            result.append(num_to_letters(v, FIRST_GROUP))
        elif k == 2:
            result.append(num_to_letters(v, SECOND_GROUP))
        elif k == 3:
            result.append(num_to_letters(v, THIRD_GROUP))
        elif k == 4:
            if int(v) > 3:
                raise ValueError("Please, consider an int between 1 and 3999")
            else:
                result.append(int(v) * "M")
    return "".join(reversed(result))
