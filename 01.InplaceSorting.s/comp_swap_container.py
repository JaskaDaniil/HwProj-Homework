"""
Container that swaps and compares
"""

from __future__ import annotations
from typing import Iterable, TypeVar
from beartype import beartype

T = TypeVar("T")


@beartype
class CompSwapList(list[T]):
    """
    A list wrapper that tracks comparison and swap operations
    """

    @property
    def swaps(self) -> int:
        """
        Return the number of swap operations performed

        :return: Number of swaps
        :rtype: int
        """
        return self._swaps

    @property
    def comps(self) -> int:
        """
        Return the number of comparison operations performed

        :return: Number of comparisons
        :rtype: int
        """
        return self._comps

    def __init__(self, data: Iterable[T]):
        """
        Initialize the container with optional initial data

        :param data: Initial data to populate the list
        :type data: Iterable[T]
        """
        super().__init__(data)

        self._swaps: int
        self._comps: int
        self.reset_stats()  # Otherwise MyPy complains unnecessarily =)

    def reset_stats(self) -> None:
        """
        Reset statistics to zero
        """
        self._swaps = 0
        self._comps = 0

    def less(self, i: int, j: int) -> bool:
        """
        Compare two elements using the < operator

        :param i: Index of the left element
        :type i: int
        :param j: Index of the right element
        :type j: int
        :return: self[i] < self[j]
        :rtype: bool
        """
        self._comps += 1
        return self[i] < self[j]  # type: ignore[operator]

    def swap(self, i: int, j: int) -> None:
        """
        Swap two elements in the list

        :param i: Index of the left element
        :type i: int
        :param j: Index of the right element
        :type j: int
        """
        self._swaps += 1
        self[i], self[j] = self[j], self[i]
