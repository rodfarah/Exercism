'''
This is the horse and the hound and the horn
that belonged to the farmer sowing his corn
that kept the rooster that crowed in the morn
that woke the priest all shaven and shorn
that married the man all tattered and torn
that kissed the maiden all forlorn
that milked the cow with the crumpled horn
that tossed the dog
that worried the cat
that killed the rat
that ate the malt
that lay in the house that Jack built.'''


def recite(start_verse, end_verse):

    object_or_animal = [
        'house that Jack built.', 'malt', 'rat', 'cat', 'dog', 'cow with the crumpled horn',
        'maiden all forlorn', 'man all tattered and torn', 'priest all shaven and shorn',
        'rooster that crowed in the morn', 'farmer sowing his corn', 'horse and the hound and the horn'
    ]

    verbs = [
        '', 'lay in the', 'ate the', 'killed the', 'worried the', 'tossed the', 'milked the',
        'kissed the', 'married the', 'woke the', 'kept the', 'belonged to the'
    ]

    # Let's create a function that creates each verse:

    def create_verse(verse_number):
        verse_list = []
        # Let's introduce the first 'actor':
        first_actor_intro = f'This is the {object_or_animal[verse_number -1]}'
        verse_list.append(first_actor_intro)
        # Let's add some actions to the list:
        while verse_number > 1:
            verse_list.append(' that ')
            verse_list.append(f'{verbs[verse_number -1]} ')
            verse_list.append(object_or_animal[verse_number - 2])
            verse_number -= 1

        return ''.join(verse_list)

    # Finally, let's iterate the arguments (start and end verse) \
    # in order create other verses using 'create_verse' function:
    result_list = []
    for verse in range(start_verse, end_verse + 1):
        result_list.append(create_verse(verse))

    return result_list


print(recite(2, 3))
