from typing import List
from math import ceil
import unittest


def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    """
    @param N: Number of seats
    @param K: spaces to left (or right) to be kept free
    @param M: current diners
    @param S: list of where each current diner is sat
    """
    S.sort()

    lowerThreshold = 1
    additionalDiners = 0

    for s in S:
        freeSpace = s - (K + 1) - lowerThreshold
        additionalDiners += freeSpace // (K + 1) + 1
        lowerThreshold = s + K + 1

    additionalDiners += (N - lowerThreshold) // (K + 1) + 1

    return additionalDiners


class getMaxAdditionalDinersCount_test(unittest.TestCase):

    inputs = [[10, 1, 2, [2, 6]], [15, 2, 3, [11, 6, 14]]]
    expected = [3, 1]

    def test(self) -> None:
        for i, input in enumerate(self.inputs):
            self.assertEqual(getMaxAdditionalDinersCount(*input), self.expected[i])


if __name__ == "__main__":
    unittest.main()
