#!/usr/bin/env python3
"""
    Function that takes two integer arguments (Advanced)
"""

import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ method that takes two integer arguments

        Args:
            page (int, optional): . Defaults to 1.
            page_size (int, optional): . Defaults to 10.

        Returns:
            List[List]: 
        """
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0
        csv_size = len(self.dataset())
        start, end = index_range(page, page_size)
        end = min(end, csv_size)
        if start >= csv_size:
            return []
        return self.dataset()[start:end]


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ it return a tuple of size two containing a start index & an end index

    Args:
        page (int): first integer arguments
        page_size (int): second integer arguments

    Returns:
        Tuple[int, int]: containing a start index and an end index
    """
    return ((page - 1) * page_size, page * page_size)
