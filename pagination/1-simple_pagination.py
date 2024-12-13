#!/usr/bin/env python3
"""
This module provides a helper function for calculating index ranges
for pagination.
"""
import csv
import math
from typing import Tuple, List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indexes for a given page and page size.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index and end index
                        for the pagination slice.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


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
        """
        Returns a page of the dataset.
        Args:
            page (int): The page number (1-indexed).
            page_size (int): The number of items per page.
        Returns:
            List[List]: The list of items on this page of the dataset.
                        An empty list if out of range.
        """
        # Vérification des arguments
        assert isinstance(page, int) and page > 0, (
            "page must be a positive integer"
        )
        assert isinstance(page_size, int) and page_size > 0, (
            "page_size must be a positive integer"
        )

        start_index, end_index = index_range(page, page_size)
        data = self.dataset()

        if start_index >= len(data):
            # Si la page demandée est hors limites, retourner une liste vide
            return []
        return data[start_index:end_index]
