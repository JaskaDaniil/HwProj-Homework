#!/usr/bin/env -S python3
"""
Sortings demo
"""
from random import shuffle


from comp_swap_container import CompSwapList
import sortings

if __name__ == "__main__":
    for n in [10, 100, 1000]:
        arr = list(range(n))
        shuffle(arr)

        # bubble_sort
        data = CompSwapList(arr)
        sortings.bubble_sort(data)
        print(n, data.comps, data.swaps)

        # quick_sort
        data = CompSwapList(arr)
        sortings.quick_sort(data)
        print(n, data.comps, data.swaps)
