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


# ------------------------------------------------------------------------------

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
