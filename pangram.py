import string

def is_pangram(sentence):

    alphabet = list(string.ascii_lowercase)
    sentence_letters = set()
    for letter in sentence:
        if letter.lower() in alphabet:
            sentence_letters.add(letter.lower())
    return len(sentence_letters) == 26
