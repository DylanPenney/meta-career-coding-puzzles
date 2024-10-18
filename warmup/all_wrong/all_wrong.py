def getWrongAnswers(N: int, C: str) -> str:
  output = ''
  for i in range (0, N):
    if C[i] == 'A':
      output += 'B'
      continue
    ouput += 'A'
  return ouput

if __name__ == "__main__":
  assert(getWrongAnswers(3, "ABA") == "BAB")
  assert(getWrongAnswers(2, "BBBBB") == "AAAAA")

