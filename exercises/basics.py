def reverse_list(l):
    """
    Reverses order of elements in list l.
    """
    return None


def test_reverse_list():
    assert reverse_list([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]


# ------------------------------------------------------------------------------

def reverse_string(s):
    """
    Reverses order of characters in string s.
    """
    return None


def test_reverse_string():
    assert reverse_string("foobar") == "raboof"


# ------------------------------------------------------------------------------

def get_word_lengths(s):
    """
    Returns a list of integers representing
    the word lengths in string s.
    """
    return None


def test_get_word_lengths():
    text = "Three tomatoes are walking down the street"
    assert get_word_lengths(text) == [5, 8, 3, 7, 4, 3, 6]


# ------------------------------------------------------------------------------

def find_longest_word(s):
    """
    Returns the longest word in string s.
    In case there are several, return the first.
    """
    return None


def test_find_longest_word():
    text = "Three tomatoes are walking down the street"
    assert find_longest_word(text) == "tomatoes"
    text = "foo foo1 foo2 foo3"
    assert find_longest_word(text) == "foo1"


# ------------------------------------------------------------------------------

def remove_substring(substring, string):
    """
    Returns string with all occurrences of substring removed.
    """
    return None


def test_remove_substring():
    assert remove_substring("don't", "I don't like cake") == "I  like cake"
    assert remove_substring("bada", "bada-bing-bada-bing") == "-bing--bing"


# ------------------------------------------------------------------------------

def read_column(file_name, column_number):
    """
    Reads column column_number from file file_name
    and returns the values as floats in a list.
    """
    return None


def test_read_column():

    import tempfile
    import os

    text = """1   0.1  0.001
2   0.2  0.002
3   0.3  0.003
4   0.4  0.004
5   0.5  0.005
6   0.6  0.006"""

    # we save this text to a temporary file
    file_name = tempfile.mkstemp()[1]
    with open(file_name, 'w') as f:
        f.write(text)

    # and now we pass the file name to the function which will read the column
    assert read_column(file_name, 2) == [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]

    # we remove the temporary file
    os.unlink(file_name)


# ------------------------------------------------------------------------------

def histogram(l):
    """
    Converts a list of tuples into a simple string histogram.
    """
    return None


def test_histogram():
    assert histogram([('a', 2), ('b', 5), ('c', 1)]) == """a: ##
b: #####
c: #"""


# ------------------------------------------------------------------------------

def character_statistics(text):
    """
    Reads text from file file_name, then
    lowercases the text, and then returns
    a list of tuples (character, occurence)
    sorted by occurence with most frequent
    appearing first.
    Use the isalpha() method to figure out
    whether the character is in the alphabet.
    """
    return None


def test_character_statistics():

    text = """
To be, or not to be: that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles,
And by opposing end them? To die: to sleep;
No more; and by a sleep to say we end
The heart-ache and the thousand natural shocks
That flesh is heir to, 'tis a consummation
Devoutly to be wish'd. To die, to sleep;
To sleep: perchance to dream: ay, there's the rub;
For in that sleep of death what dreams may come
When we have shuffled off this mortal coil,
Must give us pause: there's the respect
That makes calamity of so long life;
For who would bear the whips and scorns of time,
The oppressor's wrong, the proud man's contumely,
The pangs of despised love, the law's delay,
The insolence of office and the spurns
That patient merit of the unworthy takes,
When he himself might his quietus make
With a bare bodkin? who would fardels bear,
To grunt and sweat under a weary life,
But that the dread of something after death,
The undiscover'd country from whose bourn
No traveller returns, puzzzles the will
And makes us rather bear those ills we have
Than fly to others that we know not of?
Thus conscience does make cowards of us all;
And thus the native hue of resolution
Is sicklied o'er with the pale cast of thought,
And enterprises of great pith and moment
With this regard their currents turn awry,
And lose the name of action.--Soft you now!
The fair Ophelia! Nymph, in thy orisons
Be all my sins remember'd."""

    assert character_statistics(text) == [('e', 146), ('t', 120), ('o', 99), ('s', 88), ('a', 87),
                                          ('h', 79), ('r', 71), ('n', 70), ('i', 57), ('l', 44),
                                          ('d', 43), ('u', 41), ('f', 36), ('m', 32), ('w', 29),
                                          ('p', 24), ('c', 23), ('y', 18), ('b', 17), ('g', 14),
                                          ('k', 10), ('v', 8), ('z', 3), ('q', 2)]


# ------------------------------------------------------------------------------

def simple_zip(l1, l2):
    """
    Implement a simple zip function.
    Do not use the built-in zip().
    """
    return None


def test_simple_zip():

    assert simple_zip(['a', 'b', 'c'], [1, 2, 3]) == [('a', 1), ('b', 2), ('c', 3)]
