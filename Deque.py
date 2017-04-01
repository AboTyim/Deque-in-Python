#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# © 2017 Syrian Programmer.
#
# Deque(Double-ended_queue) are a generalization of stacks and queues
#
# Coded in Date: 1/4/2017.
#


class Deque:
    """ Python implementation the Deque """

    def __init__(self, items=None):
        if items is None:
            items = []
        self.__items = items

    def add_rear(self, item):
        self.__items.append(item)

    def add_front(self, item):
        self.__items.insert(0, item)

    def pop_front(self):
        return self.__items.pop(0)

    def pop_rear(self):
        return self.__items.pop()

    def peek_front(self):
        return self.__items[0]

    def peek_rear(self):
        return self.__items[-1]

    def reverse(self):
        self.__items.reverse()

    def extend_rear(self, items):
        self.__items.extend(items)

    def extend_front(self, items):
        for obj in reversed(items):
            self.__items.insert(0, obj)

    def clear(self):
        self.__items.clear()

    def is_empty(self):
        return self.__items == []

    def get_items(self):
        return self.__items

    def size(self):
        return len(self.__items)

    def __len__(self):
        return len(self.__items)

    def __getitem__(self, item):
        return self.__items[item]


# Sample inputs
if __name__ == '__main__':
    x = [10, 20, 30, 40, 50, 60]

    q = Deque(x)
    q.add_rear(70)
    q.add_rear(80)
    # q.reverse()
    q.extend_front([1, 2, 3, 4, 5, 6, 7, 8, 9])
    q.extend_rear([90, 100])
    print(q.get_items())
