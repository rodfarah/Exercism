def label(colors: str) -> str:
    '''To get around this problem, manufacturers print color-coded \
        bands onto the resistors to denote their resistance values. \ 
        Each band acts as a digit of a number. The program will take \ 
        3 colors as input, and outputs the correct value, in ohms. The\
        third color stands for how many zeros need to be added to the  \
        main value.So an input of "orange", "orange", "black" should    \
        return: "33 ohms"
        '''
    color_value_dict = {
        'black': 0,
        'brown': 1,
        'red': 2,
        'orange': 3,
        'yellow': 4,
        'green': 5,
        'blue': 6,
        'violet': 7,
        'grey': 8,
        'white': 9
    }

    translation = f'{color_value_dict[colors[0]]}{color_value_dict[colors[1]]}' + \
        '0'*color_value_dict[colors[2]]
    result = translation.lstrip('0')
    if result == '':
        return '0 ohms'
    elif '000000000' in result:
        return f'{result[0:-9]} gigaohms'
    elif '000000' in result:
        return f'{result[0:-6]} megaohms'
    elif '000' in result:
        return f'{result[0:-3]} kiloohms'
    else:
        return f'{result} ohms'


print(label(["black", "black", "black"]))
