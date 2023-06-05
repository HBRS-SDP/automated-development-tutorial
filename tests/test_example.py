import unittest
from automated_development_tutorial.example import fibonacci, sumOfPrimes


class TestExample(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(5), [1, 1, 2, 3, 5])
        self.assertEqual(fibonacci(6), [1, 1, 2, 3, 5])

    def test_sum_of_primes(self):
        self.assertEqual(sumOfPrimes(10), 17)


if __name__ == "__main__":
    unittest.main()
