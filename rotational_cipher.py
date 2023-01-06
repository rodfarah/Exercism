import string


def rotate(text, key):
    '''Create an implementation of the rotational cipher, \
        also sometimes called the Caesar cipher.'''

    # Creating a list of special characters:
    special_char_list = string.punctuation

    # Creating a double alphabet list (symetric, but natural doubled indexes):
    single_alphabet_list = list(string.ascii_lowercase)
    double_alphabet_list = 2 * single_alphabet_list

    # Creating a single enumerated alphabet list:
    single_alphabet_list = list(string.ascii_lowercase)

    # Proceeding to the result:
    result = []

    for character in text:
        if any([character.isspace(), character.isnumeric(), character in special_char_list]):
            result.append(character)
        elif character.isalpha() and character.isupper():
            result.append(
                double_alphabet_list[single_alphabet_list.index(character.lower()) + key].upper())
        else:
            result.append(
                double_alphabet_list[single_alphabet_list.index(character) + key])

    return ''.join(result)


print(rotate("Santa Claus is comming on 25'th December! :-)", 1))
