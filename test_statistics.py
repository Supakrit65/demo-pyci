"""This module contains test for statistics function."""

from unittest import TestCase
from statistics import variance, stdev


class StatisticsTest(TestCase):
    """This class contains test for statistics module's functions."""

    def test_variance_typical_values(self):
        """Variance of typical values."""
        self.assertEqual(0.0, variance([10.0, 10.0, 10.0, 10.0, 10.0]))
        self.assertEqual(2.0, variance([1, 2, 3, 4, 5]))
        self.assertEqual(8.0, variance([10, 2, 8, 4, 6]))

    def test_variance_throws_exception(self):
        """Variance of an empty list should raise an exception."""
        with self.assertRaises(ValueError):
            variance([])

    def test_stdev(self):
        """Test values for standard deviation."""
        # standard deviation is zero
        data = [10.0, 10.0]
        self.assertEqual(0.0, stdev(data))
        # standard deviation is 2.0
        data = [10.0, 14.0]
        self.assertEqual(2.0, stdev(data))


if __name__ == '__main__':
    import unittest

    unittest.main(verbosity=1)
