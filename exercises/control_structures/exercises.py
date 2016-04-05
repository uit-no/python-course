def simple_generator():
    pass


def test_simple_generator():
    assert list(simple_generator()) == [0, 1, 2]

    
# ------------------------------------------------------------------------------

# List comprehension
# Dictionary comprehension
# Set comprehension
# Function passing
# map()
# filter()
# Generators
# Generator comprehension

# ------------------------------------------------------------------------------


def iter_animals(lines):
    # Parse text and yield animals. Skip 'and'.
    # There will be no blank lines.
    pass


def test_iter_animals():
    text = ["""horse
        snake
        dolphin and sheep,
        bird and rabbit"""]
    
    animals = ['horse', 'snake', 'dolphin', 'sheep', 'bird', 'rabbit']

    
# ------------------------------------------------------------------------------
