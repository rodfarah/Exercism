'''In the game, five dice are rolled and the result can be entered in any of twelve categories. \
    The score of a throw of the dice depends on category chosen.
    '''


YACHT = 'YATCH'
ONES = 'ONES'
TWOS = 'TWOS'
THREES = 'THREES'
FOURS = 'FOURS'
FIVES = 'FIVES'
SIXES = 'SIXIES'
FULL_HOUSE = 'FULL_HOUSE'
FOUR_OF_A_KIND = 'FOUR_OF_A_KIND'
LITTLE_STRAIGHT = 'LITTLE_STRAIGHT'
BIG_STRAIGHT = 'BIG_STRAIGHT'
CHOICE = 'CHOICE '


def score(dice: list, category) -> int:

    simple_categories_dict = {
        ONES: 1,
        TWOS: 2,
        THREES: 3,
        FOURS: 4,
        FIVES: 5,
        SIXES: 6,
    }

    first_hypoth = len(set(dice)) == 1
    second_hypoth = len(set(dice)) == 2
    third_hypoth = len(set(dice)) == 5

    if category in simple_categories_dict.keys():
        result = 0
        for number in dice:
            if number == simple_categories_dict[category]:
                result += number
        return result
    elif category is YACHT and first_hypoth:
        return 50
    elif category is CHOICE:
        return sum(dice)
    elif category is BIG_STRAIGHT and all([third_hypoth, sum(dice) == 20]):
        return 30
    elif category is LITTLE_STRAIGHT and all([third_hypoth, sum(dice) == 15]):
        return 30
    elif second_hypoth or first_hypoth:
        for num in set(dice):
            if category is FOUR_OF_A_KIND and dice.count(num) >= 4:
                return num * 4
            elif category is FULL_HOUSE and dice.count(num) == 3:
                return sum(dice)
    return 0


print(score([3,3,3,3,3], FOUR_OF_A_KIND))
