"""
Write a random Dungeons & Dragons character generator 

Based on d10d's solution
"""

import random


ABILITIES = ("strength", "dexterity", "constitution",
             "intelligence", "wisdom", "charisma")


def modifier(constitution_score: int) -> int:
    """Return Character's constitution modifier"""
    return (constitution_score - 10) // 2


class Character:
    def __init__(self):
        for ability in ABILITIES:
            setattr(self, ability, self.ability())

        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self) -> int:
        """Rolls four 6-sided dice and return the sum of the largest three dice"""
        return sum(sorted([random.randint(1, 6) for n in range(4)])[1:])
