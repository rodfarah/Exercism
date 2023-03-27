"""Determine if a triangle is equilateral, isosceles, or scalene. 

An equilateral triangle has all three sides the same length. 
An isosceles triangle has at least two sides the same length.
A scalene triangle has all sides of different lengths.
"""


def is_triangle(func):
    """Creating a decorator in order to check if sides create a valid triangle."""
    def wrap_func(sides) -> bool:
        no_zeroes = 0 not in sides
        valid_triangle = 2 * max(sides) <= sum(sides)
        return all([no_zeroes, valid_triangle, func(sides)])
    return wrap_func


@is_triangle
def equilateral(sides: list[int]) -> bool:
    return len(set(sides)) == 1


@is_triangle
def isosceles(sides: list[int]) -> bool:
    return len(set(sides)) <= 2


@is_triangle
def scalene(sides: list[int]) -> bool:
    return len(set(sides)) == 3


print(equilateral([10, 10, 10]))
