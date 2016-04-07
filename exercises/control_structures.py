def simple_generator():
    """
    Also yield 'cow' and 'mouse'.
    """
    yield 'horse'


def test_simple_generator():
    assert list(simple_generator()) == ['horse', 'cow', 'mouse']


# ------------------------------------------------------------------------


def simple_range(limit):
    """Yield numbers from 0 up to but not including limit.
    You can use a normal while loop."""
    pass


def test_simple_range():
    assert list(simple_range(0)) == []
    assert list(simple_range(3)) == [0, 1, 2]


# ------------------------------------------------------------------------


def word_lengths(words):
    """
    Return a list of the length of each word.
    (Use len(word).)
    """
    pass


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
    return None


def test_simple_filter():

    def greater_than_ten(n):
        return n > 10

    assert simple_filter(greater_than_ten, [1, 20, 5, 13, 7, 25]) == [20, 13, 25]


# ------------------------------------------------------------------------


def simple_map(f, l):
    """
    Implement a simple map function.
    Do not use the built-in map().
    """
    return None


def test_simple_map():

    def square_me(x):
        return x*x

    assert simple_map(square_me, [1, 2, 3, 4, 5]) == [1, 4, 9, 16, 25]
