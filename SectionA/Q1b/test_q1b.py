# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals
import unittest

from q1b import *


class TestQ1b(unittest.TestCase):

    def test_transpose_3x3(self):
        """
        Test case to test transpose with 3x3 array.
        """
        lst = [
            ['L', 'E', 'D', 'R'],
            ['T', 'E', 'C', 'H'],
            ['T', 'E', 'C', 'H']
        ]
        expected_lst = [
            ['L', 'T', 'T'],
            ['E', 'E', 'E'],
            ['D', 'C', 'C'],
            ['R', 'H', 'H']
        ]
        transpose_lst = transpose(lst)
        self.assertListEqual(transpose_lst, expected_lst)

    def test_transpose_2x3(self):
        """
        Test case to test transpose with 2x3 array.
        """
        lst = [
            ['L', 'E', 'D', 'R'],
            ['T', 'E', 'C', 'H']
        ]
        expected_lst = [
            ['L', 'T'],
            ['E', 'E'],
            ['D', 'C'],
            ['R', 'H']
        ]
        transpose_lst = transpose(lst)
        self.assertListEqual(transpose_lst, expected_lst)

    def test_transpose_1x1(self):
        """
        Test case to test transpose with 1x1 array.
        """
        lst = [["LEDR", "Technology"]]
        expected_lst = [
            ['LEDR'],
            ['Technology']
        ]
        transpose_lst = transpose(lst)
        self.assertListEqual(transpose_lst, expected_lst)
