base_dict = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"
}


def one_to_999(number: int) -> str:
    """Write a number in English, from one to 999."""
    if number in base_dict:
        return base_dict[number]
    spliter_one = divmod(number, 100)
    spliter_two = divmod(spliter_one[1], 10)
    first_digit = spliter_one[0]
    second_digit = spliter_two[0]
    third_digit = spliter_two[1]
    if first_digit == 0:
        return f"{base_dict[second_digit * 10]}-{base_dict[third_digit]}"
    elif all([second_digit == 0, third_digit == 0]):
        return f"{base_dict[first_digit]} hundred"
    elif first_digit > 0 and spliter_one[1] in base_dict:
        return f"{base_dict[first_digit]} hundred {base_dict[spliter_one[1]]}"
    else:
        return f"{base_dict[first_digit]} hundred {base_dict[second_digit * 10]}-{base_dict[third_digit]}"


def say(number: int) -> str:
    """Spell out a number in English."""
    if 10e11 <= number or number < 0:
        raise ValueError("input out of range")
    elif number == 0:
        return "zero"
    str_list = "{:_}".format(number).split("_")
    order = ["", "thousand", "million", "billion"]
    inv_num_list = [int(n) for n in str_list][::-1]
    result_dict = {o: n for o, n in zip(order, inv_num_list) if n > 0}
    result_list = []
    for k, v in result_dict.items():
        if k != "":
            result_list.append(k)
        result_list.append(one_to_999(v))
    return " ".join(result_list[::-1])
