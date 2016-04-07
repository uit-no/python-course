def reverse_list(l):
    """
    Reverses order of elements in list l.
    """
    # very "pedestrian" way of doing it, without any Python niceties like
    # slicing or the reversed() generator.
    rev = []  # this will be the reversed list
    i = len(l)  # by convention, "i" usually denotes an index
    while i > 0:
        i -= 1
        rev.append(l[i])
    return rev


def reverse_list_2(l):
    # we return a list comprehension
    return [x for x in reversed(l)]


def reverse_list_3(l):
    return list(reversed(l))


def reverse_list_4(l):
    l_rev = l[:]
    l_rev.reverse()
    return l_rev


def reverse_list_5(l):
    return l[::-1]


def reverse_list_6(l):
    l_rev = []
    for x in reversed(l):
        l_rev.append(x)
    return l_rev


def reverse_list_7(l):
    l_rev = []
    for i in range(len(l)):
        l_rev.append(l[-i - 1])
    return l_rev


def reverse_string(s):
    """
    Reverses order of characters in string s.
    """
    # version of reverse_list() will happily operate on a string, but it
    # will return a list of characters ("character" == "string of length 1").
    # Now, the built-in function str.join() takes an iterable of strings and
    # puts them all together in a single string. So...
    return ''.join(reverse_list(s))


def get_word_lengths(s):
    """
    Returns a list of integers representing
    the word lengths in string s.
    """
    # We haven't learned about generators and comprehensions yet, so I'll do
    # this a bit clumsy but hopefully easy to understand.
    # str.split() takes a string and returns a list of words.
    # That is to say, it "splits the string at every white
    # space character".
    words = s.split()
    lengths = []
    for word in words:
        lengths.append(len(word))
    return lengths


def get_word_lengths_2(s):
    # s.split() splits s into words
    # len(word) gives us the length
    return [len(word) for word in s.split()]


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
    return string.replace(substring, '')


def read_column(file_name, column_number):
    """
    Reads column column_number from file file_name
    and returns the values as floats in a list.
    """
    # I will build a list holding my results, going through the file line by
    # line
    column_values = []

    # Open that (text) file and read it line by line
    fd = open(file_name, "r")  # 'fd' means 'file descriptor'... conventions...
    for line in fd.readlines():  # one line at a time...
        columns = line.split()  # split that line at the whitespaces...
        our_value_str = columns[column_number - 1]  # pick text from our column...
        our_value = float(our_value_str)  # parse the string into a float
        column_values.append(our_value)  # and append that to our result list

    fd.close()  # we politely close the door after us

    return column_values


def read_column_2(file_name, column_number):
    l = []
    # advantage of opening files with 'with'
    # is that it will automatically close
    # the file even if our code throws an
    # exception in the middle of reading
    with open(file_name, 'r') as f:
        # we do not even need f.readlines() here
        # because the file handle f already is an iterator
        for line in f:
            x = line.split()[column_number - 1]
            # we need to convert the string to a float
            l.append(float(x))
    return l


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


def histogram_2(l):
    s = ''
    for i, t in enumerate(l):
        s += '{}: {}'.format(t[0], '#' * t[1])
        if i < len(l) - 1:
            s += '\n'
    return s


# this one is even more compact and better/faster
def histogram_3(l):
    # we build a list
    # note how we immediately unpack the tuple into c, n
    s = ['{}: {}'.format(c, '#' * n) for c, n in l]
    # we join the list with newlines
    return '\n'.join(s)


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
            continue  # "NEXT!!"
        char_counts[char.lower()] += 1

    return char_counts.most_common()  # bliss


def character_statistics_2(text):
    from collections import defaultdict
    # since we want a mapping letter -> how often
    # it looks like we want to solve this with a dict
    # but instead of dict we use defaultdict
    # then we don't have to check whether the key exists
    d = defaultdict(int)
    for letter in text.lower():
        if letter.isalpha():
            d[letter] += 1
    # now we have a dictionary d where the keys are letters (unsorted)
    # and the values represent how often the letter was found
    # we convert the dict to a list of key-value tuples
    l = d.items()
    # if we would sort the list now, we would sort by letters
    # so we rearrange the tuples
    # alternatively we could sort on the second item using a lambda function
    # (see character_statistics_2)
    l_swap = [(v, k) for k, v in l]
    # now we can sort
    l_swap.sort()
    # now we unswap the tuples
    l = [(v, k) for k, v in l_swap]
    # and since it is ascending we reverse
    return list(reversed(l))


def character_statistics_3(text):
    # counter is probably the most suitable container
    from collections import Counter
    # but we do not want to count spaces and full stops etc.
    # we filter out everything that is not a letter
    regular_letters = filter(str.isalpha, [l for l in text.lower()])
    # now we a dictionary with counts
    count = Counter(regular_letters)
    # now we have a list of tuples
    l = list(count.items())
    # now let's sort the list on second items in reverse order
    l.sort(key=lambda x: x[1], reverse=True)
    # done
    return l


def simple_zip(l1, l2):
    """
    Implement a simple zip function.
    Do not use the built-in zip().
    """
    num_elems_to_zip = min(len(l1), len(l2))

    # and again... gonna make a list while iterating through another list (well,
    # two other lists, here)
    zipped = []
    i = 0  # not even going to use range()...
    while i < num_elems_to_zip:
        zipped_elem = (l1[i], l2[i])  # make the tuple
        zipped.append(zipped_elem)  # and append it to our results list
        i += 1  # don't forget this line :)

    return zipped


def simple_zip_2(l1, l2):
    l_zipped = []
    # we take min() because the shorter list determines the length
    # of the zipped list
    for i in range(min(len(l1), len(l2))):
        # the double parentheses are because we append a tuple
        l_zipped.append((l1[i], l2[i]))
    return l_zipped


def simple_zip_3(l1, l2):
    return [(l1[i], l2[i]) for i in range(min(len(l1), len(l2)))]


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


def generate_password():
    """
    Write a function that generates a random "good" password. The generated
    password should return True if checked by password_good.

    For easy to remember strong passwords see: https://xkcd.com/936/
    """
    import random  # we need randomness

    # So... I'll check what's in the 'random' module real quick that could
    # make this an easy task. sample()...
    # Here's the plan: I make passwords with sample() for as long as it takes
    # until I find one tht passes the test. It's ugly but it will work...
    # *almost* always :)
    pass_chars = "#%&0123456789abcdefghijklmnopqrstuvwxyzABCD"  # yeah enough

    while True:  # for as long as it takes...
        pw_list = random.sample(pass_chars, 8)  # make 8 letter password (get list back)
        pw = "".join(pw_list)  # still looking weird? :)
        if password_good(pw):  # check it
            return pw  # and if it passes the test, return it

    # Warning: in rare instances, this function will never return.
    # Homework: find a value for random.seed() for which this function never
    # returns.
