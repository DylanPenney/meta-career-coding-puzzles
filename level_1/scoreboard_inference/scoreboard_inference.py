from typing import List
import unittest

def getMinProblemCount(N: int, S: List[int]) -> int:
  highest_score = S[0]
  all_even = True

  for s in S:
    if s > highest_score:
      highest_score = s
    if ((all_even) and (s % 2 != 0)):
      all_even = False

  if all_even:
    return highest_score // 2
  else:
    return highest_score // 2 + 1


class getMinProblemCount_test(unittest.TestCase):

  inputs = [[6, [1, 2, 3, 4, 5, 6]], [4, [4, 3, 3, 4]], [4, [2, 4, 6, 8]]]
  expected = [4, 3, 4]

  def test(self):
    for i, input in enumerate(self.inputs):
      self.assertEqual(getMinProblemCount(*input), self.expected[i])

if __name__ == '__main__':
  unittest.main()