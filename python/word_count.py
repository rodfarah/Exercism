from string import punctuation

'''Given a phrase, count the occurrences of each word in that phrase.'''


def count_words(sentence: str) -> dict:
    symbols = ''.join(punctuation).replace("'", "")
    lower_sentence = sentence.lower()

    for symbol in symbols:
        lower_sentence = lower_sentence.replace(f'{symbol}', ' ')
    lower_sentence = lower_sentence.replace(" '", ' ').replace("' ", ' ')
    lower_sentence = lower_sentence.lstrip("'")
    lower_sentence = lower_sentence.rstrip("'")

    word_list = lower_sentence.split()
    word_set = set(word_list)
    word_count = []

    for word in word_set:
        word_count.append(word_list.count(word))

    result = {k: v for k, v in zip(word_set, word_count)}

    return result


print(count_words(",\n,one,\n ,two \n 'three'"))
