import unittest
from typing import List


def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    
    actors = []
    
    # list[i] = number of photos before index i
    photos_before_index = [0]
    backgrounds_before_index = [0]

    photo_counter = 0
    background_counter = 0

    for i in range(N):
        if C[i] == "A":
            actors.append(i)
        elif C[i] == "P":
            photo_counter += 1
        elif C[i] == "B":
            background_counter += 1

        photos_before_index.append(photo_counter)
        backgrounds_before_index.append(background_counter)

    photograph_count = 0
    for actor_pos in actors:
        # left window
        left_start = max(0, actor_pos - Y)
        left_end = max(0, actor_pos - X + 1)

        # right window
        right_start = min(N, actor_pos + X)
        right_end = min(N, actor_pos + Y + 1)

        ## Photographer - Actor - Background
        photograph_count += (
            photos_before_index[left_end] - photos_before_index[left_start]
        ) * (
            backgrounds_before_index[right_end] - backgrounds_before_index[right_start]
        )

        ## Background - Actor - Photographer
        photograph_count += (
            backgrounds_before_index[left_end] - backgrounds_before_index[left_start]
        ) * (photos_before_index[right_end] - photos_before_index[right_start])

    return photograph_count


class getArtisticPhotographCount_test(unittest.TestCase):

    inputs = [[5, "APABA", 1, 2], [5, "APABA", 2, 3], [8, ".PBAAP.B", 1, 3]]
    expected = [1, 0, 3]

    def test(self) -> None:
        for i, input in enumerate(self.inputs):
            self.assertEqual(getArtisticPhotographCount(*input), self.expected[i])


if __name__ == "__main__":
    unittest.main()
