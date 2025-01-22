import unittest

def sum(a, b):
    return a + b

class TestSum(unittest.TestCase):
    def test_sum_positive_numbers(self):
        self.assertEqual(sum(1, 2), 3)

    def test_sum_negative_numbers(self):
        self.assertEqual(sum(-1, -2), -3)

    def test_sum_positive_and_negative(self):
        self.assertEqual(sum(1, -2), -1)

    def test_sum_zero(self):
        self.assertEqual(sum(0, 0), 0)

    def test_sum_large_numbers(self):
        self.assertEqual(sum(1000000, 2000000), 3000000)

if __name__ == '__main__':
    unittest.main()