import unittest

def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    
    actors = []

    total_photographers = 0
    total_backgrounds = 0

    p_before_position = [0]
    bg_before_position = [0]

    for i in range(N):
        if C[i] == "A":
            actors.append(i)
        elif C[i] == "P":
            total_photographers += 1
        elif C[i] == "B":
            total_backgrounds += 1

        p_before_position.append(total_photographers)
        bg_before_position.append(total_backgrounds)

    artistic_photographs = 0
    for actor_pos in actors:
        # left window
        left_start = max(0, actor_pos - Y)
        left_end = max(0, actor_pos - X + 1)

        # right window
        right_start = min(N, actor_pos + X)
        right_end = min(N, actor_pos + Y + 1)

        artistic_photographs += (
            p_before_position[left_end] - p_before_position[left_start]
        ) * (
            bg_before_position[right_end] - bg_before_position[right_start]
        )

        artistic_photographs += (
            bg_before_position[left_end] - bg_before_position[left_start]
        ) * (
            p_before_position[right_end] - p_before_position[right_start]
        )

    return artistic_photographs


class getArtisticPhotographCount_test(unittest.TestCase):

    inputs = [[5, "APABA", 1, 2], [5, "APABA", 2, 3], [8, ".PBAAP.B", 1, 3]]
    expected = [1, 0, 3]

    def test(self):
        for i, input in enumerate(self.inputs):
            self.assertEqual(getArtisticPhotographCount(*input), self.expected[i])


if __name__ == "__main__":
    unittest.main()
