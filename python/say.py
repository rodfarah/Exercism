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


def below_99(str_number: str) -> str:
    """Spell out a numeral between 0 and 99."""
    if int(str_number) in one_to_nineteen:
        return one_to_nineteen[int(str_number)]

    number_list = [int(n) for n in str_number]
    if number_list[1] == 0:
        return twenty_to_ninety[number_list[0]]
    else:
        return f"{twenty_to_ninety[number_list[0]]}-{one_to_nineteen[number_list[1]]}"


def hundreds(str_number: str) -> str:
    """Spell out a numeral between 100 and 999."""
    if len(str_number) <= 2:
        return below_99(str_number)
    elif str_number == "000":
        return ""
    elif str_number.startswith("00"):
        str_number = str_number[2]
        return below_99(str_number)
    elif str_number.startswith("0"):
        str_number = str_number[1:]
        return below_99(str_number)
    number_list = [int(n) for n in str_number]
    first_digit_int = number_list[0]
    last_two_str = str_number.removeprefix(str(first_digit_int))
    if str_number[1:] == "00":
        return f"{one_to_nineteen[first_digit_int]} hundred"
    else:
        return f"{one_to_nineteen[first_digit_int]} hundred {below_99(last_two_str)}"


def slicer(str_list: list[str]) -> list[str]:
    """Return a list with characters, sliced 3 by 3."""
    str_list.reverse()
    splited_list = []
    start = 0
    end = len(str_list)
    step = 3
    for i in range(start, end, step):
        x = i
        splited_list.append(str_list[x:x+step])
    splited_list.reverse()
    master_joined = []
    for list in splited_list:
        list.reverse()
        master_joined.append("".join(l for l in list))
    return master_joined


def say(number: int) -> str:
    """Spell out a number in English."""
    str_number = str(number)
    str_number_list = [n for n in str_number]
    if number < 0 or len(str_number_list) >= 13:
        raise ValueError("input out of range")
    elif len(str_number_list) <= 2:
        return below_99(str_number)
    elif len(str_number_list) == 3:
        return hundreds(str_number)
    elif 4 <= len(str_number_list) <= 6:
        two_pieces = slicer(str_number_list)
        result = []
        result.append(f"{hundreds(two_pieces[0])} thousand")
        if two_pieces[1] != "000":
            result.append(f" {hundreds(two_pieces[1])}")
        return "".join(result)
    elif 7 <= len(str_number_list) <= 9:
        two_pieces = slicer(str_number_list)
        result = []
        result.append(f"{hundreds(two_pieces[0])} million")
        if two_pieces[1] != "000":
            result.append(f" {hundreds(two_pieces[1])} thousand")
        if two_pieces[2] != "000":
            result.append(f" {hundreds(two_pieces[2])}")
        return "".join(result)
    elif 10 <= len(str_number_list) <= 12:
        two_pieces = slicer(str_number_list)
        result = []
        result.append(f"{hundreds(two_pieces[0])} billion")
        if two_pieces[1] != "000":
            result.append(f" {hundreds(two_pieces[1])} million")
        if two_pieces[2] != "000":
            result.append(f" {hundreds(two_pieces[2])} thousand")
        if two_pieces[3] != "000":
            result.append(f" {hundreds(two_pieces[3])}")
        return "".join(result)


print(say(-1))
