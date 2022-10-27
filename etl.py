def transform(legacy_data):
    shiny_new_scrabble = dict()
    for num, letters in legacy_data.items():
        for letter in letters:
            shiny_new_scrabble[letter.lower()] = num
    return shiny_new_scrabble
