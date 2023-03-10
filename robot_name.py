"""Manage robot factory settings.
Mentored by IsaacG.
"""

import string
import random

chosen_names = set()


class Robot:
    def __init__(self):
        self.reset()

    def reset(self):
        """Reset a robot to a new unique robot name."""
        while True:
            name = ''.join(
                random.choices(string.ascii_uppercase, k=2)
                + random.choices(string.digits, k=3)
            )
            if name not in chosen_names:
                break
        chosen_names.add(name)
        self.name = name




r1 = Robot()
r2 = Robot()
print(r1.name)
print(r2.name)
r1.reset()
print(r1.name)
