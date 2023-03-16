"""Clean up user-entered phone numbers so that they can be sent SMS messages."""


class PhoneNumber:
    def __init__(self, number: str):
        """Format a phone number according to SMS standards."""
        self.number = self.validate(number)

    @property
    def area_code(self)-> str:
        """Return the area code from a phone number."""
        return self.number[0:3]

    def clean_up(self, raw_number: str) -> str:
        """Return a string with digits."""
        special_chars = " +()-."
        number_list = []
        for char in raw_number:
            if char.isalpha():
                raise ValueError("letters not permitted")
            elif char.isdigit():
                number_list.append(char)
            elif char not in special_chars:
                raise ValueError("punctuations not permitted")
        return "".join(number_list)

    def validate(self, num: str) -> str:
        """Check for ValueErrors."""
        cleaned_up_num = self.clean_up(num)
        if len(cleaned_up_num) < 10:
            raise ValueError("must not be fewer than 10 digits")
        elif len(cleaned_up_num) > 11:
            raise ValueError("must not be greater than 11 digits")
        elif len(cleaned_up_num) == 11 and not cleaned_up_num.startswith("1"):
            raise ValueError("11 digits must start with 1")
        # removes number 1 from first digit if applicable:
        elif len(cleaned_up_num) == 11:
            cleaned_up_num = cleaned_up_num.removeprefix("1")
        # new conditions after removing number 1 from first digit (if applicable):
        if cleaned_up_num[3] == "0":
            raise ValueError("exchange code cannot start with zero")
        elif cleaned_up_num[3] == "1":
            raise ValueError("exchange code cannot start with one")
        elif cleaned_up_num[0] == "0":
            raise ValueError("area code cannot start with zero")
        elif cleaned_up_num[0] == "1":
            raise ValueError("area code cannot start with one")
        return cleaned_up_num

    def pretty(self)-> str:
        """Format a phone number, using parenthesis and hyphen."""
        return f"({self.area_code})-{self.number[3:6]}-{self.number[6::]}"


p001 = PhoneNumber("(223) 456-7890")

