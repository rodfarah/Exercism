def egg_count(display_value: int) -> int:
    """Return the number of 1 bits in the binary representation of a number."""
    result_not_zero = True
    rest_list = []
    while result_not_zero:
        result = display_value//2
        rest_list.append(display_value % 2)
        if result == 0:
            result_not_zero = False
            binary = "".join(str(n) for n in reversed(rest_list))
            return binary.count("1")
        else:
            display_value = result
