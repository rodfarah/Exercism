from curses.ascii import isalpha


def is_valid(isbn):
    ''' Check if ISBN number is valid. True if:
    (d₁ * 10 + d₂ * 9 + d₃ * 8 + d₄ * 7 + d₅ * 6 + d₆ * 5 + d₇ * 4 + d₈ * 3 + d₉ * 2 + d₁₀ * 1) mod 11 == 0

    If last digit is a X, than X == 10
    '''
    # Let's create a list of numbers that excludes '-' characters:
    no_separate_dashes = [character for character in isbn if character != '-']

    # Let's check if there are 10 elements inside the list:
    if len(no_separate_dashes) != 10:
        return False

    # Let's check if the first 9 indexes are digits:
    first_nine = no_separate_dashes[: -1]
    for item in first_nine:
        if item.isalpha():
            return False

    # Let's check if the last character is a letter and if is is a 'X':
    if isbn[-1].isalpha():
        if isbn[-1] != 'X':
            return False
        else:
            no_separate_dashes.remove('X')
            no_separate_dashes.append('10')

    # Let's convert string items into integers:
    no_separate_dashes = [int(character)
                          for character in no_separate_dashes]

    # Let's create a list with multiplyer numbers:
    isbn_multiplyers_list = list(range(1, 11)[::-1])

    final_list = []

    indx_num = 0
    while indx_num <= 9:
        final_list.append(
            no_separate_dashes[indx_num]*isbn_multiplyers_list[indx_num])
        indx_num += 1

    return sum(final_list) % 11 == 0
