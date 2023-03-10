"""Clean up user-entered phone numbers so that they can be sent SMS messages."""


def clean_up(raw_number: str) -> str:
    """return a string with digits.
    raise error for alpha and peculiar characters
    """
    special_chars = ' +()-.'
    clean_number = ''
    for char in raw_number:
        if char.isdigit():
            clean_number += char
        elif char.isalpha():
            raise ValueError("letters not permitted")
        elif not char.isdigit() and char not in special_chars:
            raise ValueError("punctuations not permitted")
    return clean_number


def validation(clean_number: str) -> str:
    """check for errors.
    removes number 1 from first digit (if applicable)
    """
    if len(clean_number) < 10:
        raise ValueError("must not be fewer than 10 digits")
    elif len(clean_number) > 11:
        raise ValueError("must not be greater than 11 digits")
    elif len(clean_number) == 11 and not clean_number.startswith('1'):
        raise ValueError("11 digits must start with 1")
    # removes number 1 from first digit (if applicable):
    elif len(clean_number) == 11:
        clean_number = clean_number.removeprefix("1")
    # new conditions after removing number 1 from first digit (if applicable):
    if clean_number[3] == '0':
        raise ValueError("exchange code cannot start with zero")
    elif clean_number[3] == '1':
        raise ValueError("exchange code cannot start with one")
    elif clean_number[0] == '0':
        raise ValueError("area code cannot start with zero")
    elif clean_number[0] == '1':
        raise ValueError("area code cannot start with one")
    return clean_number


class PhoneNumber:
    def __init__(self, number: str):
        # format a phone number to send SMS:
        self.number = validation(clean_up(number))
        self.area_code = self.number[0:3]

    def pretty(self) -> str:
        """format a phone number, using parenthesis and hyphen.
        ie. (613)-995-0253
        """
        return f'({self.area_code})-{self.number[3:6]}-{self.number[6::]}'


f001 = PhoneNumber("1 (623) 43-7890")

print(f001.number)
print(f001.area_code)
print(f001.pretty())
