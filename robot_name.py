"""Manage robot factory settings."""

import string
import random


uppercase_letters = list(string.ascii_uppercase)
numbers = list(string.digits)
chosen_names = set()


class Robot:
    def __init__(self):
        self.name = self.get_name()

    def get_name(self):
        """Creates an unique random name for new or reseted robot."""
        unique_name = True
        while unique_name is True:
            two_letters = ''.join(random.choices(uppercase_letters, k=2))
            three_numbers = ''.join(random.choices(numbers, k=3))
            name = two_letters + three_numbers
            self.name = name
            if name in chosen_names:
                unique_name = False
            else:
                chosen_names.add(name)
        return name

    def reset(self):
        """Resets a robot to it's factory specs and generates a new unique robot name."""
        self.name = self.get_name()

