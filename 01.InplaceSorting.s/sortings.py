"""
Sorting algorithms
"""

from __future__ import annotations
from typing import Any
from comp_swap_container import CompSwapList


def trivial_sort2(data: CompSwapList[Any]):
    """
    Sorts a container with 2 or fewer elements

    :param data: data to sort inplace
    :type data: MutableSequence[Ordered]
    """
    if len(data) <= 1:
        pass
    if len(data) > 2:
        raise ValueError("Expected at most 2 elements!")
    if data.less(1, 0):
        data.swap(0, 1)


def bubble_sort(data: CompSwapList[Any]) -> None:
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data.less(j + 1, j):
                data.swap(j, j + 1)


def quick_sort(data: CompSwapList[Any]) -> None:
    def _qs(l: int, r: int):
        if l >= r:
            return
        pivot = r
        i = l
        for j in range(l, r):
            if data.less(j, pivot):
                data.swap(i, j)
                i += 1
        data.swap(i, pivot)
        _qs(l, i - 1)
        _qs(i + 1, r)
    _qs(0, len(data) - 1)
