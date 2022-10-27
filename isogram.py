def is_isogram(string):
    upper = string.upper()
    letters_list = []
    letters_set = set()
    for character in upper:
        if character != '-' and character != ' ':
            letters_list.append(character)
            letters_set.add(character)
    return len(letters_list) == len(letters_set)
