#!/usr/bin/env python3

import collections
from functools import wraps


def log_and_count(counts: collections.Counter, key: str = ""):
    """
    Decorator for logging and counting decorated functions' calls

    :param counts: Counter object used for counting functions' calls
    :param key: Key to use within Counter object (optional, default is name of the decorated function)

    Tests:
    >>> import collections
    ...
    >>> my_counter = collections.Counter()
    ...
    >>> @log_and_count(key='basic functions', counts=my_counter)
    ... def f1(a, b=2):
    ...     return a ** b
    >>> @log_and_count(key='basic functions', counts=my_counter)
    ... def f2(a, b=3):
    ...     return a ** 2 + b
    >>> @log_and_count(counts=my_counter)
    ... def f3(a, b=5):
    ...     return a ** 3 - b
    ...
    >>> _ = f1(2)
    called f1 with (2,) and {}
    >>> _ = f2(2, b=4)
    called f2 with (2,) and {'b': 4}
    >>> _ =f1(a=2, b=4)
    called f1 with () and {'a': 2, 'b': 4}
    >>> _ = f2(4)
    called f2 with (4,) and {}
    >>> _ = f2(5)
    called f2 with (5,) and {}
    >>> _ = f3(5)
    called f3 with (5,) and {}
    >>> _ = f3(5, 4)
    called f3 with (5, 4) and {}
    >>> print(my_counter)
    Counter({'basic functions': 5, 'f3': 2})
    """
    def outer_wrapper(logged_function):
        @wraps(logged_function)
        def inner_wrapper(*args, **kwargs):
            function_group = key if len(key) > 0 else logged_function.__name__
            counts[function_group] += 1

            print(f"called {logged_function.__name__} with {args} and {kwargs}")

            return logged_function(*args, **kwargs)

        return inner_wrapper

    return outer_wrapper


if __name__ == "__main__":
    import doctest

    doctest.testmod()
