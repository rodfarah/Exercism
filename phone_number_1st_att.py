'''Clean up user-entered phone numbers so that they can be sent SMS messages.'''


class PhoneNumber:
    def __init__(self, number: str):
        special_chars = ' +()-.'
        clean_number = ''
        for char in number:
            if char.isalpha():
                raise ValueError("letters not permitted")
            elif not char.isdigit() and char not in special_chars:
                raise ValueError("punctuations not permitted")
            elif char.isdigit():
                clean_number += char
        if len(clean_number) < 10:
            raise ValueError("must not be fewer than 10 digits")
        elif len(clean_number) > 11:
            raise ValueError("must not be greater than 11 digits")
        elif len(clean_number) == 11 and not clean_number.startswith('1'):
            raise ValueError("11 digits must start with 1")
        # removes number 1 from first digit if applicable:
        elif len(clean_number) == 11:
            clean_number = clean_number.removeprefix("1")
        if clean_number[3] == '0':
            raise ValueError("exchange code cannot start with zero")
        elif clean_number[3] == '1':
            raise ValueError("exchange code cannot start with one")
        elif clean_number[0] == '0':
            raise ValueError("area code cannot start with zero")
        elif clean_number[0] == '1':
            raise ValueError("area code cannot start with one")
        self.number = clean_number

        self.area_code = clean_number[0:3]
        
    def pretty(self):
        return f'({self.area_code})-{self.number[3:6]}-{self.number[6::]}'
    
p001 = PhoneNumber("+1 (613)-995-0253")

print(p001.number)
print(p001.area_code)
print(p001.pretty())
