#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    '''max_integer tests'''
    def test_max_integer(self):
        '''possible tests'''
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

        self.assertEqual(max_integer([90, 30, 100, 40]), 100)

        self.assertEqual(max_integer([99999, 2, -3, -99999]), 99999)

        self.assertEqual(max_integer([0, 0, 0, 0]), 0)

        self.assertEqual(max_integer([]), None)

        self.assertEqual(max_integer([5]), 5)

        self.assertEqual(max_integer([5, 5.5, 6, 6.6]), 6.6)


if __name__ == '__main__':
    unittest.main()
