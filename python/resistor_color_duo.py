color_list = [
    'Black',
    'Brown',
    'Red',
    'Orange',
    'Yellow',
    'Green',
    'Blue',
    'Violet',
    'Grey',
    'White'
]

def cap_first(word):
    return word.capitalize()


def value(colors):
    el = []
    caps_list = map(cap_first, colors)
    for color in caps_list:
        for final_color in color_list:
            if color == final_color:
                el.append(color_list.index(color))
    return el[0] * 10 + el[1]


print(value(['black', 'brown']))