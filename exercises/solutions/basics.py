def reverse_list(l):
    """
    Reverses order of elements in list l.
    """
    # we return a list comprehension
    return [x for x in reversed(l)]


def reverse_list_2(l):
    return list(reversed(l))


def reverse_list_3(l):
    l_rev = l[:]
    l_rev.reverse()
    return l_rev


def reverse_list_4(l):
    return l[::-1]


def reverse_list_5(l):
    l_rev = []
    for x in reversed(l):
        l_rev.append(x)
    return l_rev


def reverse_list_6(l):
    l_rev = []
    for i in range(len(l)):
        l_rev.append(l[-i-1])
    return l_rev


def reverse_string(s):
    """
    Reverses order of characters in string s.
    """
    # reverse_list can also work on a string
    # however it produces a list which we need
    # to join back into a string
    return ''.join(reverse_list(s))


def get_word_lengths(s):
    """
    Returns a list of integers representing
    the word lengths in string s.
    """
    # s.split() splits s into words
    # len(word) gives us the length
    return [len(word) for word in s.split()]


def find_longest_word(s):
    """
    Returns the longest word in string s.
    In case there are several, return the first.
    """
    longest = ''
    for word in s.split():
        if len(word) > len(longest):
            longest = word
    return longest


def remove_substring(substring, string):
    """
    Returns string with all occurrences of substring removed.
    """
    # we replace substring by nothing
    return string.replace(substring, '')


def read_column(file_name, column_number):
    """
    Reads column column_number from file file_name
    and returns the values as floats in a list.
    """
    l = []
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
    s = ''
    for i, t in enumerate(l):
        s += '{}: {}'.format(t[0], '#'*t[1])
        if i < len(l) - 1:
            s += '\n'
    return s


# this one is more compact and better/faster
def histogram_2(l):
    # we build a list
    # note how we immediately unpack the tuple into c, n
    s = ['{}: {}'.format(c, '#'*n) for c, n in l]
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


def character_statistics_2(text):
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
    l_zipped = []
    # we take min() because the shorter list determines the length
    # of the zipped list
    for i in range(min(len(l1), len(l2))):
        # the double parentheses are because we append a tuple
        l_zipped.append((l1[i], l2[i]))
    return l_zipped


def simple_zip_2(l1, l2):
    return [(l1[i], l2[i]) for i in range(min(len(l1), len(l2)))]
