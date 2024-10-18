from typing import List
import unittest

def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
  number_of_battleships = 0
  total_spaces = R * C

  for row in G:
    for column in row:
      if column == 1:
        number_of_battleships += 1
  
  return number_of_battleships / total_spaces

class getHistProbability_test(unittest.TestCase):
  
  inputs = [[2, 3, [[0, 0, 1], [1, 0, 1]]], [2, 2, [[1, 1], [1, 1]]]]
  expected = [0.5, 1.00]

  def test(self):
    for i in range(0, min(len(self.inputs), len(self.expected))):
      self.assertEqual(getHitProbability(self.inputs[i][0], self.inputs[i][1], self.inputs[i][2]), self.expected[i])

if __name__ == '__main__':
  unittest.main() 