#!/usr/bin/env python3
"""
function named index_range that takes two integer
arguments page and page_size
"""
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    function named index_range that takes two integer
    arguments page and page_size
    """
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    return start_idx, end_idx
