import unittest

def getUniformIntegerCountInInterval(A: int, B: int) -> int:
    # find the uniform number that is in the form of the first digit repeated for both A and B
    # then determine whether it is higher or lower than the respective A or B

    digits_A = getDigitsFromInteger(A)
    digits_B = getDigitsFromInteger(B)

    for i in range(len(digits_A) - 2, -1, -1):
        if digits_A[i] > digits_A[-1]:
            # A is higher than the uniform number, find the next uniform number, by increasing the first digit by 1
            digits_A[-1] += 1
            break

        if digits_A[i] < digits_A[-1]:
            break

    for i in range(len(digits_B) - 2, -1, -1):
        if digits_B[i] < digits_B[-1]:
            # B is lower than the uniform number, find the next uniform number, by decreasing the first digit by 1
            digits_B[-1] -= 1
            break

        if digits_B[i] > digits_B[-1]:
            break

    uniform_numbers_less_than_A = (9 * (len(digits_A) - 1)) + digits_A[-1]
    uniform_numbers_less_than_B = (9 * (len(digits_B) - 1)) + digits_B[-1]

    return uniform_numbers_less_than_B - uniform_numbers_less_than_A + 1


def getDigitsFromInteger(N: int) -> list:
    digits = []
    while N > 0:
        digits.append(N % 10)
        N //= 10
    return digits


class getUniformIntegerCountInInteval_test(unittest.TestCase):

    inputs = [[75, 300], [1, 9], [999999999999, 999999999999]]
    expected = [5, 9, 1]

    def test(self):
        for i, input in enumerate(self.inputs):
            self.assertEqual(getUniformIntegerCountInInterval(*input), self.expected[i])


if __name__ == "__main__":
    unittest.main()
