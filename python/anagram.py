from collections import Counter


def find_anagrams(word, candidates):

    word = word.lower()

    # Creating a "candidates dict" where Keys are "Case sensitive" and Values are strictly "lower". One condition: word and candidate must have the same letter counter!
    real_candidates_dict = {candidate: candidate.lower() for candidate in candidates if candidate.lower(
    ) != word and Counter(word) == Counter(candidate.lower())}

    # Creating a set of letters of the Word in order to compare sets (words and candidates) in next step.
    word_set = set(letter for letter in word)

    # Creating an empty set and then adding "Case Sensitive" candidates (keys from above dict) into it, since candidate is subset of word.
    result = set()

    for caps_matter, caps_off in real_candidates_dict.items():
        if set(letter for letter in caps_off).issubset(word_set):
            result.add(caps_matter)
    return result


print(find_anagrams('stone', {'stone', 'notes'}))
