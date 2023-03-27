'''In the game, five dice are rolled and the result can be entered in any of twelve categories. \
    The score of a throw of the dice depends on category chosen.
    PS: I have solved this exercise before, using only pure function. Bellow I will solve it using OOP
    '''


class Game:
    def __init__(self, dice: list):
        self.dice = dice

        self.first_hypoth = len(set(dice)) == 1
        self.second_hypoth = len(set(dice)) == 2
        self.third_hypoth = len(set(dice)) == 5

    def ONES(self, dice):
        result = []
        for number in dice:
            if number == 1:
                result.append(number)
        return sum(result)

    def TWOS(self, dice):
        result = []
        for number in dice:
            if number == 2:
                result.append(number)
        return sum(result)

    def THREES(self, dice):
        result = []
        for number in dice:
            if number == 3:
                result.append(number)
        return sum(result)

    def FOURS(self, dice):
        result = []
        for number in dice:
            if number == 4:
                result.append(number)
        return sum(result)

    def FIVES(self, dice):
        result = []
        for number in dice:
            if number == 5:
                result.append(number)
        return sum(result)

    def SIXES(self, dice):
        result = []
        for number in dice:
            if number == 6:
                result.append(number)
        return sum(result)

    def YATCH(self):
        if self.first_hypoth:
            return 50
        return 0

    def CHOICE(self, dice):
        return sum(dice)

    def BIG_STRAIGHT(self, dice):
        if self.third_hypoth and sum(dice) == 15:
            return 30
        return 0

    def LITTLE_STRAIGHT(self, dice):
        if self.third_hypoth and sum(dice) == 20:
            return 30
        return 0

    def FOUR_OF_A_KIND(self, dice):
        for num in set(dice):
            if all([self.second_hypoth, dice.count(num) == 4]):
                return num * 4
            return 0

    def FULL_HOUSE(self, dice):
        for num in set(dice):
            if all([self.second_hypoth, dice.count(num) == 3]):
                return sum(dice)
            return 0


def score(dice, category):

    yatch = Game(dice)

    if category == 'ONES':
        return yatch.ONES(dice)
    elif category == 'TWOS':
        return yatch.TWOS(dice)
    elif category == 'THREES':
        return yatch.THREES(dice)
    elif category == 'FOURS':
        return yatch.FOURS(dice)
    elif category == 'FIVES':
        return yatch.FIVES(dice)
    elif category == 'SIXES':
        return yatch.SIXES(dice)
    elif category == 'YATCH':
        return yatch.YATCH(dice)
    elif category == 'CHOICE':
        return yatch.CHOICE(dice)
    elif category == 'BIG_STRAIGHT':
        return yatch.BIG_STRAIGHT(dice)
    elif category == 'LITTLE_STRAIGHT':
        return yatch.LITTLE_STRAIGHT(dice)
    elif category == 'FOUR_OF_A_KIND':
        return yatch.FOUR_OF_A_KIND(dice)
    elif category == 'FULL_HOUSE':
        return yatch.FULL_HOUSE(dice)


print(score([1, 2, 3, 4, 5], 'BIG_STRAIGHT'))
