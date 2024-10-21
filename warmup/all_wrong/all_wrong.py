import unittest

def getWrongAnswers(N: int, C: str) -> str:
  output = ''
  for i in range (0, N):
    if C[i] == 'A':
      output += 'B'
      continue
    output += 'A'
  return output

class getWrongAnswers_test(unittest.TestCase):
  inputs = [[3, "ABA"], [5, "BBBBB"]]
  expected = ["BAB", "AAAAA"]

  def test(self) -> None:
    for i in range(0, min(len(self.inputs), len(self.expected))):
      self.assertEqual(getWrongAnswers(self.inputs[i][0], self.inputs[i][1]), self.expected[i])

if __name__ == "__main__":
  unittest.main()

