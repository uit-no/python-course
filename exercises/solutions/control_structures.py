def simple_generator():
    """
    Also yield 'cow' and 'mouse'.
    """
    yield 'horse'
    # just going to do it...
    yield 'cow'
    yield 'mouse'


def test_simple_generator():
    assert list(simple_generator()) == ['horse', 'cow', 'mouse']


# ------------------------------------------------------------------------


def simple_range(limit):
    """Yield numbers from 0 up to but not including limit.
    You can use a normal while loop."""
    i = 0
    while i < limit:
        yield i
        i += 1


def test_simple_range():
    assert list(simple_range(0)) == []
    assert list(simple_range(3)) == [0, 1, 2]


# ------------------------------------------------------------------------


def word_lengths(words):
    """
    Return a list of the length of each word.
    (Use len(word).)
    """
    # a simple list comprehension does the job.
    return [ len(word) for word in words ]
    # Note that we had a very similar exercise yesterday where you had to
    # do this without a list comprehension (get_word_lengths())


def test_word_lengths():
    words = ['lorem', 'ipsum', 'python', 'sit', 'amet']
    lengths = [5, 5, 6, 3, 4]
    assert word_lengths(words) == lengths


# ------------------------------------------------------------------------


def simple_filter(f, l):
    """
    Implement a simple filter function.
    Do not use the built-in filter().
    """
    # a list comprehension with an 'if' clause goes the job nicely
    return [ item for item in l if f(item) ]


def simple_filter_2(f, l):
    """
    Implement a simple filter function.
    Do not use the built-in filter().
    """
    # alternative implementation: the same as above, but without comprehension.
    filtered_l = []
    for item in l:
        if f(item):
            filtered_l.append(item)
    return filtered_l
    # I think the list comprehension is not only shorter, but also more
    # readable.


def test_simple_filter():

    def greater_than_ten(n):
        return n > 10

    assert simple_filter(greater_than_ten, [1, 20, 5, 13, 7, 25]) == [20, 13, 25]
    assert simple_filter_2(greater_than_ten, [1, 20, 5, 13, 7, 25]) == [20, 13, 25]


# ------------------------------------------------------------------------


def simple_map(f, l):
    """
    Implement a simple map function.
    Do not use the built-in map().
    """
    # Again, my first take is a list comprehension.
    return [ f(item) for item in l ]


def simple_map_2(f, l):
    """
    Implement a simple map function.
    Do not use the built-in map().
    """
    # Same as above without comprehension:
    mapped_l = []
    for item in l:
        mapped_l.append( f(item) ) # the extra blanks are just for readability
    return mapped_l


def test_simple_map():

    def square_me(x):
        return x*x

    assert simple_map(square_me, [1, 2, 3, 4, 5]) == [1, 4, 9, 16, 25]
    assert simple_map_2(square_me, [1, 2, 3, 4, 5]) == [1, 4, 9, 16, 25]
