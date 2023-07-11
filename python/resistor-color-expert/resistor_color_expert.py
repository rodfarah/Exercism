
VALUES = {"black": "0",
          "brown": "1",
          "red": "2",
          "orange": "3",
          "yellow": "4",
          "green": "5",
          "blue": "6",
          "violet": "7",
          "grey": "8",
          "white": "9"
          }

TOLERANCE = {"grey": "0.05",
             "violet": "0.1",
             "blue": "0.25",
             "green": "0.5",
             "brown": "1",
             "red": "2",
             "gold": "5",
             "silver": "10"
             }


def remove_zeros(number: str) -> str:
    """Given a string of a number (ie. "52000"), remove zeros from right to left (ie. "52")"""
    while True:
        if number.endswith("0"):
            number = number.removesuffix("0")
        else:
            break
    return number


def resistor_label(colors: str) -> str:
    """Translate resistor color bands to human-readable labels, considering maximum tolerance"""
    if len(colors) == 1:
        return f"{VALUES[colors[0]]} ohms"
    else:
        tolerance = TOLERANCE[colors[-1]]
        multiplier = VALUES[colors[-2]]

        base_idx = len(colors) - 3
        values_list = []
        while base_idx >= 0:
            values_list.append(VALUES[colors[base_idx]])
            base_idx -= 1
        value_wo_zeroes = "".join([value for value in values_list[::-1]])
        value_w_zeroes = value_wo_zeroes + ("0" * int(multiplier))
    lenght = len(value_w_zeroes)
    edited_wo_zeroes = remove_zeros(value_w_zeroes)
    if lenght < 4:
        return f"{value_w_zeroes} ohms ±{tolerance}%"
    elif lenght >= 4:
        if lenght == 4:
            if int(value_w_zeroes) % 1000 == 0:
                return f"{edited_wo_zeroes} kiloohms ±{tolerance}%"
            else:
                return f"{edited_wo_zeroes[0:1]}.{edited_wo_zeroes[1:]} kiloohms ±{tolerance}%"
        elif lenght == 5:
            if int(value_w_zeroes) % 1000 == 0:
                return f"{edited_wo_zeroes} kiloohms ±{tolerance}%"
            else:
                return f"{edited_wo_zeroes[0:2]}.{edited_wo_zeroes[2:]} kiloohms ±{tolerance}%"
        elif lenght == 6:
            if int(value_w_zeroes) % 1000 == 0:
                return f"{edited_wo_zeroes} kiloohms ±{tolerance}%"
            else:
                return f"{edited_wo_zeroes[0:3]}.{edited_wo_zeroes[3:]} kiloohms ±{tolerance}%"
        elif lenght == 7:
            if int(value_w_zeroes) % 1000000 == 0:
                return f"{edited_wo_zeroes} megaohms ±{tolerance}%"
            else:
                return f"{edited_wo_zeroes[0:1]}.{edited_wo_zeroes[1:]} megaohms ±{tolerance}%"
        elif lenght == 8:
            if int(value_w_zeroes) % 1000000 == 0:
                return f"{edited_wo_zeroes} megaohms ±{tolerance}%"
            else:
                return f"{edited_wo_zeroes[0:2]}.{edited_wo_zeroes[2:]} megaohms ±{tolerance}%"
