'''In the game, five dice are rolled and the result can be entered in any of twelve categories. \
    The score of a throw of the dice depends on category chosen.
    I've tried this algorithm bellow, which I think is pretty good, but it does not follow the \
    logic the authors asked.
    So, I tried using OOP, but again the same logic problem.
    So, I tried one more try and now it is ok (please, see yatch.py).
    '''


def score(dice: list, category: str) -> int:

    simple_categories_dict = {
        'ONES': 1,
        'TWOS': 2,
        'THREES': 3,
        'FOURS': 4,
        'FIVES': 5,
        'SIXES': 6,
    }

    first_hypoth = len(set(dice)) == 1
    second_hypoth = len(set(dice)) == 2
    third_hypoth = len(set(dice)) == 5

    if category in simple_categories_dict.keys():
        result = []
        for number in dice:
            if number == simple_categories_dict[category]:
                result.append(number)
        return sum(result)
    elif category == 'YATCH' and first_hypoth:
        return 50
    elif category == 'CHOICE':
        return sum(dice)
    elif category == 'BIG_STRAIGHT' and all([third_hypoth, sum(dice) == 15]):
        return 30
    elif category == 'LITTLE_STRAIGHT' and all([third_hypoth, sum(dice) == 20]):
        return 30
    elif second_hypoth:
        for num in set(dice):
            if category == 'FOUR_OF_A_KIND' and dice.count(num) == 4:
                return num * 4
            elif category == 'FULL_HOUSE' and dice.count(num) == 3:
                return sum(dice)
    else:
        return 0


print(score([3, 3, 3, 3, 3], 'YATCH'))
