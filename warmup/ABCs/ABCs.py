import unittest

def getSum(A: int, B: int, C: int) -> int:
  return A + B + C

class getSum_test(unittest.TestCase):
  inputs = [[1, 2, 3], [100, 100, 100], [85, 16, 93]]
  expected = [6, 300, 194]
  
  def test(self) -> None:
    for i in range(0, min(len(self.inputs), len(self.expected))):
      self.assertEqual(getSum(self.inputs[i][0], self.inputs[i][1], self.inputs[i][2]), self.expected[i])

if __name__ == "__main__":
  unittest.main()
