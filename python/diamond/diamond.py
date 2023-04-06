"""Given a letter, print a diamond starting with 'A', with the supplied letter at the widest point."""
import string


def rows(letter: str) -> str:
    """Print a diamond starting with 'A', with the supplied letter at the widest point."""
    if letter == "A":
        return ["A"]
    alphabet = list(string.ascii_uppercase)
    letter_idx = alphabet.index(letter)
    num_of_points = (letter_idx + 1) * 2 - 1
    first_line = alphabet[0].center(num_of_points, " ")
    lines = [first_line]
    back_forward = 1
    for n in range(letter_idx):
        each_line = []
        for char in range(num_of_points):
            if char == letter_idx + back_forward or char == letter_idx - back_forward:
                each_line.append(alphabet[back_forward])
            else:
                each_line.append(" ")
        lines.append("".join(each_line))
        back_forward += 1
    inverted = lines[-2::-1]
    return lines + inverted
