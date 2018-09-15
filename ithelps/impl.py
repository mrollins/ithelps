#!/usr/bin/env python3
import itertools as it
from typing import Iterable

def munch(iterable: Iterable, n: int):
    """
    Consume an iterable in sequential n-length chunks.

    >>> [list(x) for x in munch([1, 2, 3, 4], 2)]
    [[1, 2], [3, 4]]

    :param iterable: sequence to iterate.
    :param n: int - Chunk length.
    :return: Iterator
    """

    args = [iter(iterable)] * n
    return zip(*args)


def slide(iterable: Iterable, n: int):
    """
    Slide an n-length window over an iterable.

    >>> [list(x) for x in slide([1, 2, 3, 4], 2)]
    [[1, 2], [2, 3], [3, 4]]

    :param iterable: Sequence to iterate.
    :param n: int - Window length.
    :return: Iterator
    """
    iterators = it.tee(iterable, n)
    for i, iterator in enumerate(iterators):
        for _ in range(i):
            next(iterator, None)
    return zip(*iterators)
