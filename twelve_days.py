'''return the lyrics of the song: "The Twelve Days of Christmas."'''


def recite(start_verse: int, end_verse: int) -> str:
    number_gift_dict = {
        1: 'a Partridge in a Pear Tree.',
        2: 'two Turtle Doves',
        3: 'three French Hens',
        4: 'four Calling Birds',
        5: 'five Gold Rings',
        6: 'six Geese-a-Laying',
        7: 'seven Swans-a-Swimming',
        8: 'eight Maids-a-Milking',
        9: 'nine Ladies Dancing',
        10: 'ten Lords-a-Leaping',
        11: 'eleven Pipers Piping',
        12: 'twelve Drummers Drumming'
    }
    number_position_dict = {
        1: 'first',
        2: 'second',
        3: 'third',
        4: 'fourth',
        5: 'fifth',
        6: 'sixth',
        7: 'seventh',
        8: 'eighth',
        9: 'ninth',
        10: 'tenth',
        11: 'eleventh',
        12: 'twelfth'
    }

    result = []

    for n in range(start_verse, end_verse + 1):
        each_full_string = f'On the {number_position_dict[n]} day of Christmas my true love gave to me: '
        if n == 1:
            each_full_string += number_gift_dict[n]
            result. append(each_full_string)
            continue
        for verse in range(n, 1, -1):
            each_full_string += number_gift_dict[verse] + ', '
        each_full_string += f'and {number_gift_dict[1]}'
        result.append(each_full_string)
    return result


print(recite(12, 12))
