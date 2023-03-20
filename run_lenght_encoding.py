"""Implement run-length encoding and decoding."""


def decode(string: str) -> str:
    """Decode a string (RLE)"""
    if string == "":
        return ""
    else:
        for item in string:
            if not (item.isalnum() or item.isspace()):
                raise ValueError("characters must be letters or integers")

    result_list = []
    idx = 0
    while idx <= len(string) - 1:
        if not string[idx].isdigit():
            result_list.append(string[idx])
            idx += 1
        else:
            if string[idx+1].isdigit():
                result_list.append(
                    int(string[idx]+string[idx+1]) * string[idx + 2]
                )
                idx += 3
            else:
                result_list.append(int(string[idx]) * string[idx+1])
                idx += 2
    return "".join(result_list)


def encode(string: str) -> str:
    """Encode a string (RLE)"""
    if string == "":
        return ""
    else:
        for item in string:
            if not (item.isalnum() or item.isspace()):
                raise ValueError("characters must be letters or integers")

    base_char = [string[0]]
    idx = 1
    result_list = []
    for char in string[1:]:
        if char in base_char:
            base_char.append(char)
            idx += 1
        else:
            result_list.append(str(len(base_char)))
            result_list.append(base_char[0])
            base_char = [char]
            idx += 1
    result_list.append(str(len(base_char)))
    result_list.append(base_char[0])
    for item in result_list:
        if item == "1":
            result_list.remove(item)
    return "".join(result_list)


# print(encode("AAARRRCDDA"))
print(decode("12WB12W3B24WB"))
# WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB
