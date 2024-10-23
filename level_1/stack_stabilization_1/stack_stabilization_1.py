from typing import List
import unittest

def getMinimumDeflatedDiscCount(N: int, R: List[int]) -> int:
    deflated_disks = 0
    # loop from bottom to top
    for i in range(N-1, 0, -1):
      # impossible to fix
      if R[i] <= i:
          return -1
      
      if R[i] <= R[i - 1]:
          R[i-1] = R[i] - 1 # make just the right size
          deflated_disks += 1
    return deflated_disks

class getMinimumDeflatedDiscCount_test(unittest.TestCase):

    inputs = [[5, [2, 5, 3, 6, 5]], [3, [100, 100, 100]], [4, [6, 5, 4, 3]]]
    expected = [3, 2, -1]

    def test(self):
        for i, input in enumerate(self.inputs):
            self.assertEqual(getMinimumDeflatedDiscCount(*input), self.expected[i])

if __name__ == '__main__':
    unittest.main()