"""Given a string of digits, output all the contiguous substrings of length n
in that string in the order that they appear.
"""


def slices(series: str, length: int) -> list[str]:
    """return a list of series slices"""
    if series == '':
        raise ValueError('series cannot be empty')
    elif length > len(series):
        raise ValueError('slice length cannot be greater than series length')
    elif length == 0:
        raise ValueError('slice length cannot be zero')
    elif length < 0:
        raise ValueError('slice length cannot be negative')

    result = []

    while len(series) >= length:
        idx = 0
        combination = ''
        while idx < length:
            combination += series[idx]
            idx += 1
        result.append(combination)
        series = series.removeprefix(series[0])

    return result


print(slices('12345', 6))
