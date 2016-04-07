# Disclaimer: I tried to solve the exercises without using any advanced
# language constructs that you'll learn about a bit later.


def reverse_list(l):
    """
    Reverses order of elements in list l.
    """
    # very "pedestrian" way of doing it, without any Python niceties like
    # slicing or the reversed() generator.
    rev = [] # this will be the reversed list
    i = len(l) # by convention, "i" usually denotes an index
    while i > 0:
        i -= 1
        rev.append(l[i])
    return rev
    


def test_reverse_list():
    assert reverse_list([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]


# ------------------------------------------------------------------------------

def reverse_string(s):
    """
    Reverses order of characters in string s.
    """
    # my version of reverse_list() will happily operate on a string, but it
    # will return a list of characters ("character" == "string of length 1").
    # Now, the built-in function str.join() takes an iterable of strings and
    # puts them all together in a single string. So...
    return "".join(reverse_list(s))


def test_reverse_string():
    assert reverse_string("foobar") == "raboof"


# ------------------------------------------------------------------------------

def get_word_lengths(s):
    """
    Returns a list of integers representing
    the word lengths in string s.
    """
    # We haven't learned about generators and comprehensions yet, so I'll do
    # this a bit clumsy but hopefully easy to understand
    words = s.split() # str.split() takes a string and returns a list of words.
                      # That is to say, it "splits the string at every white
                      # space character".
    lengths = []
    for word in words:
        lengths.append(len(word))
    return lengths


def test_get_word_lengths():
    text = "Three tomatoes are walking down the street"
    assert get_word_lengths(text) == [5, 8, 3, 7, 4, 3, 6]


# ------------------------------------------------------------------------------

def find_longest_word(s):
    """
    Returns the longest word in string s.
    In case there are several, return the first.
    """
    # the classical pattern when we search for an extreme value in an iterable:
    # 1) initialize variable holding what we search for with a "zero" value
    longest_word = ""
    # 2) iterate thorugh iterable, and for every item in the iterable...
    for word in s.split():
        # ...might the item we're looking at be the one we're looking for?
        if len(word) > len(longest_word):
            longest_word = word
    # after the loop, we can be certain that 'longest_word' holds the longest
    # word.
    return longest_word


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
    # I didn't want to figure out how to do this. It's not really hard for an
    # experienced programmer, but then again it's not super easy either. So I
    # just checked what methods a string object has, and lo and behold, there's
    # a method called "replace", which does all the hard work for me so that I
    # don't have to. Hooray for "batteries included".
    #
    # str.replace(what_to_replace, what_to_replace_it_with) does what is asked
    # from us here.
    return string.replace(substring, "")


def test_remove_substring():
    assert remove_substring("don't", "I don't like cake") == "I  like cake"
    assert remove_substring("bada", "bada-bing-bada-bing") == "-bing--bing"


# ------------------------------------------------------------------------------

def read_column(file_name, column_number):
    """
    Reads column column_number from file file_name
    and returns the values as floats in a list.
    """
    # I will build a list holding my results, going through the file line by
    # line
    column_values = []

    # Open that (text) file and read it line by line
    fd = open(file_name, "r") # 'fd' means 'file descriptor'... conventions...
    for line in fd.readlines(): # one line at a time...
        columns = line.split() # split that line at the whitespaces...
        our_value_str = columns[column_number - 1] # pick text from our column...
        our_value = float(our_value_str) # parse the string into a float
        column_values.append(our_value) # and append that to our result list
    
    fd.close() # we politely close the door after us

    return column_values


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
    # I'll make a list of strings, one string for each line. Then I'll join
    # them together, with line-breaks between them.
    lines = []
    for name, number in l:
        # I go piece-wise through a list, making another list in the process.
        # Notice the pattern? This is what we do _very_ often. So often, in
        # fact, that we will soon learn about ways to write this more concisely
        line = name + ": " + (number * "#")
        lines.append(line)

    # let's join the lines together, using "\n" (line-break) as the separator
    # between them. In Python, you just do this like so:
    result = "\n".join(lines)
    # as soon as the "\n".join(lines) bit stops looking a bit weird to you, you
    # "get" Python... until then, "just do it".

    return result


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
    # So, no collections.Counter or collections.defaultdict? Nope. I'll allow
    # this. collections.Counter shall do all the hard bits so I don't have to:

    import collections
    char_counts = collections.Counter()
    for char in text:
        if not char.isalpha():
            continue # "NEXT!!"
        char_counts[char.lower()] += 1
    
    return char_counts.most_common() # bliss


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
    num_elems_to_zip = min(len(l1), len(l2))

    # and again... gonna make a list while iterating through another list (well,
    # two other lists, here)
    zipped = []
    i = 0 # not even going to use range()...
    while i < num_elems_to_zip:
        zipped_elem = (l1[i], l2[i]) # make the tuple
        zipped.append(zipped_elem) # and append it to our results list
        i += 1 # don't forget this line :)

    return zipped


def test_simple_zip():

    assert simple_zip(['a', 'b', 'c'], [1, 2, 3]) == [('a', 1), ('b', 2), ('c', 3)]


# ------------------------------------------------------------------------------

def password_good(password):
    """
    Implement a function that tests if the input string is a "good" password.

    A "good" password should:

    - Be at least 8 characters long
    - Contain at least one upper-case letter [A-Z]
    - Contain at least one lower-case letter [a-z]
    - Contain at least one digit [0-9]
    - Contain at least one special character [#%&]

    The function should return True if the password is good, False otherwise.
    """
    # I'll do those checks one after another. A password is good only if it
    # passes all the checks.

    # check for minimum length
    if len(password) < 8:
        return False

    # check for at least one upper-case letter
    uppercase_found = False
    for char in password:
        if char.isupper():
            uppercase_found = True
            break
    if not uppercase_found:
        return False

    # check for at least one lower-case letter.
    # Note that we could do this in the loop above - in fact we probably should
    # because we hate repeating ourselves. But I said I'd go through the checks
    # one after another and not convoluted so that's what I'm gonna do.
    lowercase_found = False
    for char in password:
        if char.islower():
            lowercase_found = True
            break
    if not lowercase_found:
        return False

    # Okay, two more checks looking for some sort of character. Fuck it. I'll do
    # both in one loop now.
    digit_found = False
    special_found = False
    for char in password:
        if char.isdigit():
            digit_found = True
        elif char in "#%&":
            special_found = True
        # note that we don't break out of the loop, because we're looking for
        # more than one thing. We can, though, when we know we found
        # everything.  Usually I wouldn't do it in order to avoid unnecessary
        # code for very little gain (we're going through a password, not
        # terabytes of data). But just to demonstrate it:
        if digit_found and special_found:
            break
    if not (digit_found and special_found):
        return False

    # Still here? Not returned False yet? Then the password has passed all the
    # tests.
    return True


def test_password_good():

    good_passwords = ['Aa0#abcd', 'Zz9&0000', 'ABrt#&%aabb00']

    for pw in good_passwords:
        assert password_good(pw)

    bad_passwords = ['Aa0#', 'Zz9&000', 'ABrtaabb00', 'rt#&%aabb00',
                     'AB#&%001', 'ABrt#&%aabb']

    for pw in bad_passwords:
        assert not password_good(pw)


# ------------------------------------------------------------------------------

def generate_password():
    """
    Write a function that generates a random "good" password. The generated
    password should return True if checked by password_good.

    For easy to remember strong passwords see: https://xkcd.com/936/
    """
    import random # we need randomness

    # So... I'll check what's in the 'random' module real quick that could
    # make this an easy task. sample()...
    # Here's the plan: I make passwords with sample() for as long as it takes
    # until I find one tht passes the test. It's ugly but it will work...
    # *almost* always :)
    pass_chars = "#%&0123456789abcdefghijklmnopqrstuvwxyzABCD" # yeah enough
    
    while True: # for as long as it takes...
        pw_list = random.sample(pass_chars, 8) # make 8 letter password (get list back)
        pw = "".join(pw_list) # still looking weird? :)
        if password_good(pw): # check it
            return pw # and if it passes the test, return it

    # Warning: in rare instances, this function will never return.
    # Homework: find a value for random.seed() for which this function never
    # returns.


def test_generate_password():

    # generate list of 10 random passwords
    pw_list = []
    for _ in range(10):
        pw_list.append(generate_password())

    # passwords should be random, test for duplicates
    assert len(pw_list) == len(set(pw_list))

    # test all passwords in list
    for pw in pw_list:
        assert password_good(pw)
