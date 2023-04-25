"""
Given an input text output it transposed.

Very well mentored by MatthijsBlom.
"""

from itertools import zip_longest


def no_terminal_none(any_list: list) -> list:
    """Extract eventual terminal None s from a list"""
    while any_list and any_list[-1] is None:
        any_list.pop()
    return any_list


def transpose(lines: str) -> str:
    """Transpose a string input."""
    splited_lines = lines.split("\n")

    # Isolate each character from each line and put them inside respective lists
    splited_lines_lists = [list(item) for item in splited_lines]

    # Transpose and combine isolated characters into tuples, already with Nones (if aplicable)
    equal_len_tuples = zip_longest(*splited_lines_lists)

    # Delete None s if situated at the end
    no_last_none = [no_terminal_none(list(item)) for item in equal_len_tuples]

    # Convert residual None s into blank spaces
    none_to_space = [[" " if char is None else char for char in comb]
                     for comb in no_last_none]

    # Final answer
    joined = ("".join(lst) for lst in none_to_space)
    return "\n".join(joined)
