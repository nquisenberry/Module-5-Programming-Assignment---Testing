import unittest


def sum(arg):
    total = 0
    for val in arg:
        total += val
    return total


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 5, "Should be 5")


if __name__ == "__main__":
    unittest.main()

""" The test results show that the sum() function is working correctly.
The first test checks that adding the numbers 1, 2, and 3 returns 6.
The second test checks that adding the values in a tuple returns 5.
Since both tests passed and the output says "OK", it means the function
returned the expected results for each test case. If one of the tests
had failed, it would mean that there is a problem in the function's
logic and the code would need to be reviewed and corrected. """