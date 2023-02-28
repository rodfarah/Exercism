# Score categories.
# Change the values as you see fit.

simple_categories_dict = {
    'ONES': 1,
    'TWOS': 2,
    'THREES': 3,
    'FOURS': 4,
    'FIVES': 5,
    'SIXES': 6,
}

# complex_categories_dict = {
#     'FULL_HOUSE' : None,
#     'FOUR_OF_A_KIND' : None,
#     'LITTLE_STRAIGHT' : None,
#     'BIG_STRAIGHT' : None,
#     'CHOICE' : None,
#     'YACHT' : None
# }


def score(dice: list, category: str) -> int:

    ordered_list = sorted(dice)
    first_condition = len(set(ordered_list)) == 1
    second_condition = ordered_list[0] = 1
    third_condition = ordered_list[0] = 2

    if category in simple_categories_dict.keys():
        result = []
        for number in dice:
            if number == simple_categories_dict[category]:
                result.append(number)
        return sum(result)
    elif category == 'YATCH':
        if len(set(dice)) == 1:
            return 50
    elif category == 'CHOICE':
        return sum(dice)
    elif category == 'BIG_STRAIGHT' and all(first_condition, )

print(score([1, 1, 2, 1, 1], 'TWOS'))
