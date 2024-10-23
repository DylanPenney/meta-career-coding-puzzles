from typing import List
import unittest


def getSecondsRequired(N: int, F: int, P: List[int]) -> int:
    return N - min(P)


class getSecondsRequired_test(unittest.TestCase):

    inputs = [[3, 1, [1]], [6, 3, [5, 2, 4]]]
    expected = [2, 4]

    def test(self):
        for i, input in enumerate(self.inputs):
            self.assertEqual(getSecondsRequired(*input), self.expected[i])


if __name__ == "__main__":
    unittest.main()
