# https://www.codewars.com/kata/515bb423de843ea99400000a


import math


class PaginationHelper:

    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    def item_count(self):
        return len(self.collection)

    def page_count(self):
        return int(math.ceil(self.item_count()/self.items_per_page))

    def page_item_count(self, page_index):
        if page_index not in range(0, self.page_count()):
            return -1
        elif page_index == self.page_count() - 1 and self.item_count() % self.items_per_page != 0:
            return self.item_count() % self.items_per_page
        else:
            return self.items_per_page

    def page_index(self, item_index):
        if item_index not in range(0, self.item_count()):
            return -1
        return int(math.ceil((item_index + 1)/self.items_per_page)) - 1


collection = list('abcdef')
