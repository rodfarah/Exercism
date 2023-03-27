one_to_nineteen = {
    0: "zero",
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
    19: "nineteen"
}

twenty_to_ninety = {
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety"
}


def zero_to_99(number: int) -> str:
    """Spell out a number in English from zero to 99."""
    
    if number in one_to_nineteen:
        return one_to_nineteen[number]
    sliced = divmod(number, 10)
    if sliced[1] == 0:
        return f"{twenty_to_ninety[sliced[0]]}"
    else:        
        return f"{twenty_to_ninety[sliced[0]]}-{one_to_nineteen[sliced[1]]}"


def hundred_to_999(number: int) -> str:
    """Spell out a number in English, from 100 to 999."""
    if number < 100:
        return zero_to_99(number)
    slicer = divmod(number, 100)
    if slicer[1] == 0:
        return f"{one_to_nineteen[slicer[0]]} hundred"
    else:
        return f"{one_to_nineteen[slicer[0]]} hundred " + zero_to_99(slicer[1])


result = []
def slicer(number: int) -> list[int]:
    """Return a list with sliced 3 by 3 digits from a large number."""
    sliced = divmod(number, 1000)
    result.append(sliced[1])
    if sliced[0] > 999:
        slicer(sliced[0])
    result.append(sliced[0])
    for num in result:
        if num > 999:
            result.remove(num)
    return result


def say(number: int) -> str:
    """Spell out a number in English."""
    if 10e11 <= number or number < 0:
        raise ValueError("input out of range")
    elif number == 0:
        return zero_to_99(number)
    num_list = slicer(number)
    order = ["", "thousand", "million", "billion"]
    result_dict = {n: o for n, o in zip(num_list, order) if n > 0}
    result_list = []
    for k, v in result_dict.items():
        result_list.append(v)
        result_list.append(hundred_to_999(k))
    return " ".join(result_list[::-1])
