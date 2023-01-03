def is_triangle(sides):
    a, b, c = sides
    if a == 0 or b == 0 or c == 0:
        return False
    elif a + b >= c and b + c >= a and a + c >= b:
        return True
    else:
        return False


def equilateral(sides):
    if is_triangle(sides) == False:
        return False
    elif len(set(sides)) == 1:
        return True
    return False


def isosceles(sides):
    if is_triangle(sides) == False:
        return False
    elif 1 <= len(set(sides)) <= 2:
        return True
    return False


def scalene(sides):
    if is_triangle(sides) == False:
        return False
    if len(set(sides)) == 3:
        return True
    return False
