# isdgoijsijg

def simple_generator():
    pass


def test_simple_generator():
    assert list(simple_generator()) == [0, 1, 2]


# ------------------------------------------------------------------------


def simple_range(limit):
    pass


def test_simple_range():
    assert list(simple_range(2)) == [0, 1]
    assert list(simple_range(3)) == [0, 1, 2]


# ------------------------------------------------------------------------


# List comprehensions.

def word_lengths(words):
    return [len(word) for word in words]


def test_word_lengths():
    assert word_lengths()


# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------

# List comprehension
# Dictionary comprehension
# Set comprehension
# Function passing
# map()
# filter()
# Generators
# Generator comprehension

