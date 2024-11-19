from typing import List
import unittest


def getMaxExpectedProfit(N: int, V: List[int], C: int, S: float) -> float:
    if S == 0.00:
        # if packages are never stolen then we should enter once at the end
        return sum(V) - C

    # use dynamic programming
    dp = [0] * (N + 1)

    V = [0] + V

    for i in range(1, N + 1):
        v, s = 0, 1
        dp[i] = -float("inf")
        for j in range(i - 1, -1, -1):
            dp[i] = max(dp[i], dp[j] + V[i] + v - C)
            s *= 1 - S
            v += V[j] * s

    return max(dp)


class getMaxExpectedProfit_test(unittest.TestCase):

    inputs = [
        [5, [10, 2, 8, 6, 4], 5, 0.0],
        [5, [10, 2, 8, 6, 4], 5, 1.0],
        [5, [10, 2, 8, 6, 4], 3, 0.5],
        [5, [10, 2, 8, 6, 4], 3, 0.15],
    ]
    expected = [25.00000000, 9.00000000, 17.00000000, 20.10825000]

    def test(self):
        for i, input in enumerate(self.inputs):
            self.assertAlmostEqual(getMaxExpectedProfit(*input), self.expected[i])