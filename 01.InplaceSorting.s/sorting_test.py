"""
Unit tests for 00.Demo
"""

import random
from itertools import pairwise
import pytest
from comp_swap_container import CompSwapList
import sortings


@pytest.fixture(scope="module")
def fatal_array():
    """
    Create a shuffled array of 1000 elements with fixed seed
    """
    r = random.Random()
    r.seed(123456)

    data = list(range(1000))
    r.shuffle(data)
    yield CompSwapList(data)


def test_trivial_sort2():
    """
    Test trivial sorting of a 2-element array
    """
    a2: CompSwapList[int] = CompSwapList([2, 1])
    sortings.trivial_sort2(a2)
    assert all(x <= y for x, y in pairwise(a2))


def test_some_sorting(fatal_array):
    """
    Test some sorting algorithm
    """
    # replace with a call to a sorting algorithm
    # that uses `less` and `swap`
    sortings.quick_sort(fatal_array)

    assert all(x <= y for x, y in pairwise(fatal_array))
