#!/usr/bin/env python3
# vim:set nospell:
"""
Implements the sixth challenge, part 2.

Author: Wolfgang Richter <wolfgang.richter@gmail.com>

Copyright 2017 Wolfgang Richter, under the MIT License.
"""


from typing import List


TESTS = [([0, 2, 7, 0], 4), ([10,0], 2)]


def rebalance(banks: List[int]) -> int:
    """
    Solves the AOC sixth puzzle, part two.
    """

    oldbanks = set()
    oldbankl = []
    cycles = 0
    length = len(banks)

    while tuple(banks) not in oldbanks:
        oldbanks.add(tuple(banks))
        oldbankl.append(tuple(banks))

        maxvalue = max(banks)
        maxindex = banks.index(maxvalue)
        index = maxindex

        banks[maxindex] = 0

        while maxvalue > 0:
            index = (index + 1) % length

            if index == maxindex:
                continue

            banks[index % length] += 1
            maxvalue -= 1

        cycles += 1

    return cycles - oldbankl.index(tuple(banks))


def test_rebalance() -> None:
    """
    This tests the rebalance function by running through a list of
    hard-coded test cases.
    """
    for test in TESTS:
        assert rebalance(test[0]) == test[1]


if __name__ == '__main__':
    test_rebalance()

    TARGET = '''5 1   10  0   1   7   13  14  3   12  8   10  7   12  0   6'''

    print(rebalance([int(i) for i in TARGET.split()]))
