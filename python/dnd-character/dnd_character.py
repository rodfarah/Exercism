"""Write a random character generator """

import random


def score() -> int:
    """Rolls four 6-sided dice and return the sum of the largest three dice"""
    return sum(sorted([random.randint(1, 6) for n in range(4)])[1:])

ABILITIES = ("strenght", "dexterity", "constitution", "intelligence", "wisdom", "charisma")
             
def modifier(constitution_score: int) -> int:
    """Return Character's constitution modifier"""
    return (constitution_score - 10) // 2

class Character:
    def __init__(self):
        for ability in ABILITIES:
            setattr(self, ability, score())
        
        self.hitpoints = 10 + modifier(self.constitution)


c1 = Character()


print(c1.strenght, c1.dexterity, c1.constitution, c1.intelligence, c1.wisdom, c1.charisma)
