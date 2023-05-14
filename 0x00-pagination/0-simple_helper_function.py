#!/usr/bin/env python3
"""
contains a func `index_range` that
takes two integer arg `page` and `page_size`
"""


def index_range(page: int, page_size: int) -> tuple:
    """does what the comment says"""
    last_idx = page * page_size

    first_idx = last_idx - page_size

    return (first_idx, last_idx)
