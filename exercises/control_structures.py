def simple_generator():
    pass


def test_simple_generator():
    assert list(simple_generator()) == [0, 1, 2]


# ---------------------------------------------------------------------------


# List comprehensions.

def remove_sheep(animals):
    """Returns a list of animals without any sheep."""
    pass


def test_remove_sheep():
    animals = ['horse', 'duck', 'sheep', 'pig', 'sheep', 'sheep']
    no_sheep = ['horse', 'duck', 'pig']
    assert remove_sheep(animals) == no_sheep


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

