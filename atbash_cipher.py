from string import ascii_lowercase, punctuation

'''Create an implementation of the atbash cipher, an ancient encryption \
    system created in the Middle East.
    Plain:  abcdefghijklmnopqrstuvwxyz
    Cipher: zyxwvutsrqponmlkjihgfedcba
    Ciphertext is written out in groups of fixed length, the traditional group \ 
    size being 5 letters, leaving numbers unchanged, and punctuation is excluded. 
'''

regular_alphabet = ''.join(ascii_lowercase)
reversed_alphabet = regular_alphabet[::-1]
symbols = ''.join(punctuation)

reg_rev_alpha = dict(zip(regular_alphabet, reversed_alphabet))
rev_reg_alpha = dict(zip(reversed_alphabet, regular_alphabet))


def encode(plain_text: str) -> str:
    plain_text = plain_text.lower()

    preliminar = ''

    for character in plain_text:
        if character.isspace() or character in symbols:
            preliminar += ''
        elif character.isdigit():
            preliminar += character
        else:
            preliminar += reg_rev_alpha[character]

    idx_char_prelim_dict = {k: v for k, v in enumerate(preliminar, 1)}

    multiples_of_five = len(preliminar) // 5

    for num in range(1, multiples_of_five + 1):
        for k, v in idx_char_prelim_dict.items():
            if k == num*5:
                idx_char_prelim_dict[k] += ' '

    result = ''
    for k, v in idx_char_prelim_dict.items():
        result += v
    return result.rstrip()


def decode(ciphered_text: str) -> str:
    plain_text = ciphered_text.lower()

    result = ''

    for character in plain_text:
        if character.isspace() or character in symbols:
            result += ''
        elif character.isdigit():
            result += character
        else:
            result += rev_reg_alpha[character]
    return result


print(encode("The quick brown fox jumps over the lazy dog."))
