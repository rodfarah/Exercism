import string


def del_symbols(phrase):
    special_chars = string.punctuation.replace("'", "")

    for character in phrase:
        if character in special_chars:
            clear_word = phrase.replace(character, ' ')
            return clear_word.replace('  ', ' ')
    return phrase


def abbreviate(words):
    words_without_symbols = del_symbols(words)
    sep_words_list = words_without_symbols.split(' ')
    result_list = [word[0] for word in sep_words_list if len(word) > 0]
    return ''.join(letter.upper() for letter in result_list)

