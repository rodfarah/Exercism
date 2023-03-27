vowel_sounds = ['a', 'e', 'i', 'o', 'u', 'y', 'w']
special_consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j',
                      'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'z']
cluster2 = ['bl', 'cl', 'fl', 'gl', 'pl', 'sl', 'br', 'cr', 'dr', 'fr',
            'gr', 'pr', 'tr', 'sc', 'sk', 'sm', 'sn', 'sp', 'st', 'sw', 'tw', 'ch', 'rh', 'th']
cluster3 = ['sch', 'shr', 'spl', 'squ', 'thr', 'spr', 'scr', 'sph']


def translate_each_one(text: str):

    first_letter = text[0]
    second_letter = text[1]

    for triple in cluster3:
        if text.startswith(triple):
            return text[3:] + text[0:3] + 'ay'

    for double in cluster2:
        if text.startswith(double):
            return text[2:] + text[0:2] + 'ay'

    if text.startswith('xr') or text.startswith('ea'):
        return text + 'ay'
    if first_letter in vowel_sounds:
        if second_letter in vowel_sounds:
            return text[1:] + first_letter + 'ay'
        else:
            return text + 'ay'
    elif text.startswith('qu'):
        return text[2:] + 'quay'
    if len(text) > 2:
        third_letter = text[2]
        if all([first_letter in special_consonants, second_letter == 'q', third_letter == 'u']):
            return text[3:] + text[0:4] + 'y'
    return text[1:] + first_letter + 'ay'


def translate(text: str):
    if ' ' in text:
        split_text_list = text.split(' ')
        result_str = ''
        idx = 0
        while idx < len(split_text_list):
            result_str += translate_each_one(split_text_list[idx]) + ' '
            idx += 1
        return result_str[:-1]
    else:
        return translate_each_one(text)


print(translate('quick fast run'))
# ythmrhay
