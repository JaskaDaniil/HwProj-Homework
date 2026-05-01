"""
Test comp & swap list
"""

from comp_swap_container import CompSwapList


def test_cl_ops():
    """
    Test comp & swap list
    """
    l: CompSwapList = CompSwapList([3, 2, 1])
    assert not l.less(0, 1)
    l.swap(0, 1)
    assert l.less(0, 1)
    assert l.comps == 2
    assert l.swaps == 1
