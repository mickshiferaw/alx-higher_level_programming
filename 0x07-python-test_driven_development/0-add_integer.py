#!/usr/bin/python3
def add_integer(a, b=98):
    """this function compute and return the sum of two numbers

    Args:
        a (int): A number represents the first argument
        b (int): A number represents the second argument
    Returns:
        int: A number representing the arithmentic sum of 'a' and 'b'
    """
    # if a is False:
    #     raise TypeError("Missing argument")
    if isinstance(a, str) and isinstance(b, str):
        raise TypeError("a and b must be an integer")
    if isinstance(a, str) or a is None:
        raise TypeError("a must be an integer")
    if isinstance(b, str) or b is None:
        raise TypeError("b must be an integer")
    if isinstance(a or b, int) or isinstance(a or b, float):
        return int(a + b)
