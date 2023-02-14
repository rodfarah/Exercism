def score(word):

    letter_values = {
        1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
        2: ["D", "G"],
        3: ["B", "C", "M", "P"],
        4: ["F", "H", "V", "W", "Y"],
        5: ["K"],
        8: ["J", "X"],
        10: ["Q", "Z"]
    }

    values = []
    for letter in word.upper():
        for k, v in letter_values.items():
            if letter in v:
                values.append(k)

    return sum(values)


print(score('cabbage'))
