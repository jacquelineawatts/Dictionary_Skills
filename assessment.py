"""Dictionaries Assessment

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""


def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """

    word_dict = {}
    words = phrase.split(' ')

    for word in words:
        word_dict[word] = word_dict.get(word, 0) + 1
    return word_dict

    # Really tried hard to get this to fit within a dict comprehension, but
    # given comprehensions save output as a new dict, couldn't reference the
    # dict name in the get method. Is there a way to resolve that?

    # i.e. word_dict = {word: word_dict.get(word, 0) + 1 for word in words}

def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon

    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25

        >>> get_melon_price('Tomato')
        'No price found'
    """

    melons = {
        'Watermelon': 2.95,
        'Cantaloupe': 2.50,
        'Musk': 3.25,
        'Christmas': 14.25
        }


    if melon_name in melons:
        return melons[melon_name]
    else:
        return 'No price found'

#------------------------- ALTERNATIVE SOLUTION -----------------------------
    # SHORTER, tho perhaps a little less readable for quickly scanning

    # return melons[melon_name] if melon_name in melons else "No price found"


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]
    """

    word_lengths = {}

    # Added 'word length: list of words' as key, value pairs to dictionary
    for word in words:
        if len(word) in word_lengths:
            word_lengths[len(word)].append(word)
        else:
            word_lengths[len(word)] = [word]

    # Returned list comprehension of tuple key value pairs sorted by word length and by words
    return [(length, sorted(word_list)) for length, word_list in sorted(word_lengths.items())]



def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """

    pirate_dict = {
        'sir': 'matey',
        'hotel': 'fleabag inn',
        'student': 'swabbie',
        'man': 'matey',
        'professor': 'foul blaggart',
        'restaurant': 'galley',
        'your': 'yer',
        'excuse': 'arr',
        'students': 'swabbies',
        'are': 'be',
        'restroom': 'head',
        'my': 'me',
        'is': 'be'}

    words = phrase.split(' ')
    new_phrase = [pirate_dict[word] if word in pirate_dict else word for word in words]

    return " ".join(new_phrase)



def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    Another example:

        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """
    # Create dictionary with key, value pairs of name: (first letter, last letter)
    names_dict = {name:(name[0], name[-1]) for name in names}

    # Establish first name as the seed, and create empty results list.
    name, f_letter, l_letter = names[0], names[0][0], names[0][-1]
    results = []

    # Define conditions required to add next name to list
    while name not in results and l_letter == name[-1]:

        # Append name to results and create list of words that meet criteria of first letter
        # being equal to last letter of preceeding word
        results.append(name)
        potential_next_names = [name for name, letters in names_dict.items() if letters[0] == l_letter]

        # Filter through names to find those in the potenial next list not yet used
        # (looped thru names rathe rthan potential next names to ensure correct order)
        for name in names:
            if name in potential_next_names and name not in results:

                # When next name used, reassign variables to be used again from top of while loop
                name = name
                l_letter = name[-1]
                break

    return results


#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
