def getSum(A: int, B: int, C: int) -> int:
  return A + B + C;

if __name__ == "__main__":
  assert(getSum(1, 2, 3) == 6)
  assert(getSum(100, 100, 100) == 300)
  assert(getSum(85, 16, 93) == 194)
