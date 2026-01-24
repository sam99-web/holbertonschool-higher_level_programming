#!/usr/bin/python3
"""
Unittest for max_integer function.

This module contains unittest test cases for the max_integer([..]) function.
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function."""

    def test_regular_list(self):
        """Test with a regular list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_single_element(self):
        """Test with a list containing only one element."""
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([-5]), -5)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertIsNone(max_integer([]))
        self.assertIsNone(max_integer())

    def test_negative_numbers(self):
        """Test with negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-10, -5, -20, -3]), -3)

    def test_positive_and_negative(self):
        """Test with both positive and negative numbers."""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([100, -200, 50, -10]), 100)

    def test_all_same_values(self):
        """Test with all elements being the same."""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)
        self.assertEqual(max_integer([0, 0, 0]), 0)
        self.assertEqual(max_integer([-3, -3, -3]), -3)

    def test_max_at_beginning(self):
        """Test when max is at the beginning."""
        self.assertEqual(max_integer([10, 1, 2, 3]), 10)
        self.assertEqual(max_integer([100, 50, 25, 10]), 100)

    def test_max_at_middle(self):
        """Test when max is in the middle."""
        self.assertEqual(max_integer([1, 10, 2, 3]), 10)
        self.assertEqual(max_integer([5, 100, 50]), 100)

    def test_max_at_end(self):
        """Test when max is at the end."""
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)
        self.assertEqual(max_integer([50, 75, 100]), 100)

    def test_large_numbers(self):
        """Test with very large numbers."""
        self.assertEqual(max_integer([1000000, 999999, 500000]), 1000000)
        self.assertEqual(max_integer([10**9, 10**8, 10**7]), 10**9)

    def test_floats(self):
        """Test with floating point numbers."""
        self.assertEqual(max_integer([1.5, 2.7, 3.2, 1.1]), 3.2)
        self.assertEqual(max_integer([-1.5, -2.7, -0.5]), -0.5)

    def test_mixed_int_and_float(self):
        """Test with mixed integers and floats."""
        self.assertEqual(max_integer([1, 2.5, 3, 1.5]), 3)
        self.assertEqual(max_integer([10, 9.9, 10.1, 9]), 10.1)

    def test_zero_in_list(self):
        """Test with zero in the list."""
        self.assertEqual(max_integer([0, 1, 2, 3]), 3)
        self.assertEqual(max_integer([-5, 0, -3]), 0)
        self.assertEqual(max_integer([0, 0, 0, 1]), 1)

    def test_two_elements(self):
        """Test with only two elements."""
        self.assertEqual(max_integer([1, 2]), 2)
        self.assertEqual(max_integer([2, 1]), 2)
        self.assertEqual(max_integer([-5, -10]), -5)

    def test_long_list(self):
        """Test with a long list."""
        long_list = list(range(1, 1001))
        self.assertEqual(max_integer(long_list), 1000)
        
        long_list_reverse = list(range(1000, 0, -1))
        self.assertEqual(max_integer(long_list_reverse), 1000)

    def test_duplicate_max(self):
        """Test when the max value appears multiple times."""
        self.assertEqual(max_integer([5, 10, 10, 3]), 10)
        self.assertEqual(max_integer([10, 5, 10, 10]), 10)


if __name__ == '__main__':
    unittest.main()
