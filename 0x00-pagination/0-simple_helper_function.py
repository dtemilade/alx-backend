#!/usr/bin/env python3
"""
    Function that takes two integer arguments
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ it return a tuple of size two containing a start index & an end index

    Args:
        page (int): first integer arguments
        page_size (int): second integer arguments

    Returns:
        Tuple[int, int]: containing a start index and an end index
    """
    return ((page - 1) * page_size, page * page_size)
