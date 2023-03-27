class Luhn:
    def __init__(self, card_num: str) -> bool:
        self.card_num = card_num.replace(" ", "")

    def valid(self):
        """Return whether or not a number is valid per the Luhn formula."""
        if len(self.card_num) <= 1:
            return False
        for char in self.card_num:
            if not char.isdigit():
                return False
        inverted_firsts = [int(n) for n in self.card_num[-1::-2]]
        inverted_seconds = [int(n) for n in self.card_num[-2::-2]]
        test_seconds = map(lambda n: n*2-9 if n*2 >
                           9 else n*2, inverted_seconds)
        return (sum(inverted_firsts) + sum(list(test_seconds))) % 10 == 0
