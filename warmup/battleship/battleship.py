from typing import List

def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
  number_of_battleships = 0
  total_spaces = R * C

  for row in G:
    for column in row:
      if column == 1:
        number_of_battleships += 1
  
  return number_of_battleships / total_spaces
