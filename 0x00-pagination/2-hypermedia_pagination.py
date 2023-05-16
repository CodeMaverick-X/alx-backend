#!/usr/bin/env python3
"""implemented get_hyper
"""
import csv
from math import ceil
from typing import List, Dict


def index_range(page: int, page_size: int) -> tuple:
    """does what the comment says"""
    last_idx = page * page_size

    first_idx = last_idx - page_size

    return (first_idx, last_idx)


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
        """return data for a page"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        st_idx, end_idx = index_range(page, page_size)
        return self.dataset()[st_idx:end_idx]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """hyper media pagination"""
        page_dic = {}
        page_dic['page_size'] = page_size
        page_dic['page'] = page
        page_dic['data'] = self.get_page(page, page_size)

        next_page = page + 1 if self.get_page(page + 1,
                                              page_size) != [] else None
        prev_page = (page - 1
                     if page - 1 != 0
                     and self.get_page(page - 1, page_size) != []
                     else None)

        page_dic['next_page'] = next_page
        page_dic['prev_page'] = prev_page

        page_dic['total_pages'] = ceil(len(self.dataset()) / page_size)

        return page_dic
