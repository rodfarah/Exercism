colors_and_numbers = {
    "Black": 0,
    "Brown": 1,
    "Red": 2,
    "Orange": 3,
    "Yellow": 4,
    "Green": 5,
    "Blue": 6,
    "Violet": 7,
    "Grey": 8,
    "White": 9}


def color_code(color):
    maiusc = color.capitalize()
    for cor in colors_and_numbers:
        if cor == maiusc:
            return colors_and_numbers.get(cor)


def colors():
    colors_list = [color.lower() for color in colors_and_numbers]
    return colors_list
