# From codereview.stackexchange.com
import functools
import operator
import numpy as np


def partitions(set_):
    if not set_:
        yield []
        return
    for i in range(2**len(set_)//2):
        parts = [list(), list()]
        for item in set_:
            parts[i & 1].append(item)
            i >>= 1
        for b in partitions(parts[1]):
            yield [parts[0]]+b


def get_partitions(set_):
    for partition in partitions(set_):
        yield [list(elt) for elt in partition]
