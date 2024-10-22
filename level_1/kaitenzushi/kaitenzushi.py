from typing import List
import unittest


def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
    
    pile = {}
    eaten = 0
    for dish in D:
      last_time = pile.get(dish)
      if last_time is None or eaten - last_time >= K:
        eaten += 1
        pile[dish] = eaten # update the last time this dish has been eaten
        
    return eaten


class getMaximumEatenDishCount_test(unittest.TestCase):

    inputs = [
        [6, [1, 2, 3, 3, 2, 1], 1],
        [6, [1, 2, 3, 3, 2, 1], 2],
        [7, [1, 2, 1, 2, 1, 2, 1], 2],
    ]
    expected = [5, 4, 2]

    def test(self) -> None:
        for i, input in enumerate(self.inputs):
            self.assertEqual(getMaximumEatenDishCount(*input), self.expected[i])

if __name__ == "__main__":
    unittest.main()