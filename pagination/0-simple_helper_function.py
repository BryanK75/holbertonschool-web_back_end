#!/usr/bin/env python3
"""
This module provides a helper function for calculating index ranges
for pagination.
"""
from typing import Tuple


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
