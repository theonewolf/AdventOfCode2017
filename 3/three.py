#!/usr/bin/env python3
# vim:set nospell:
"""
Implements the third challenge.

Author: Wolfgang Richter <wolfgang.richter@gmail.com>

Copyright 2017 Wolfgang Richter, under the MIT License.
"""


from math import ceil, floor, sqrt


TESTS = [(1, 0), (12, 3), (23, 2), (17, 4), (4, 1), (5, 2), (9, 2), (16, 3),
         (25, 4), (1024, 31)]


def distance(index: int) -> int:
    """
    Solves the AOC third puzzle.
    """
    manhattan = 0

    if index == 1:
        return manhattan

    cycle = int(ceil(sqrt(index)))
    reference = cycle * cycle
    midpoint = ceil((2 * reference - cycle + 1) / 2)

    count = 0
    while index < reference - (cycle - 1):
        reference -= cycle - 1
        if count % 2 == 0:
            midpoint = floor((2 * reference - cycle + 1) / 2)
        else:
            midpoint = ceil((2 * reference - cycle + 1) / 2)
        count += 1

    manhattan += abs(index - midpoint)

    if cycle <= 4:
        manhattan += floor(sqrt(cycle))
    else:
        manhattan += floor(cycle / 2)

    return manhattan


def test_distance() -> None:
    """
    This tests the distance function by running through a list of
    hard-coded test cases.
    """
    for test in TESTS:
        assert distance(test[0]) == test[1]


if __name__ == '__main__':
    test_distance()

    TARGET = 289326

    print(distance(TARGET))
