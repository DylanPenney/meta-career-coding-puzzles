from contextlib import AbstractContextManager
from typing import Any, List
import unittest


def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
    prev = 1
    entry_time = 0
    for c in C:
        entry_time += min((c - prev) % N, (prev - c) % N)
        prev = c
    return entry_time


class getMinCodeEntryTime_test(unittest.TestCase):

    inputs = [[3, 3, [1, 2, 3]], [10, 4, [9, 4, 4, 8]]]
    expected = [2, 11]

    def test(self) -> None:
        for i, input in enumerate(self.inputs):
            self.assertEqual(getMinCodeEntryTime(*input), self.expected[i])


if __name__ == "__main__":
    unittest.main()
