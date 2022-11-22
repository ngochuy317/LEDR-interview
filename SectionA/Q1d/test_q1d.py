# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals
import unittest

from q1d import *


class TestQ1d(unittest.TestCase):

    def test_int_to_string(self):
        """
        Test case to test int_to_string.
        """
        str_val = int_to_string(1)
        self.assertEqual(str_val, "01")
        str_val = int_to_string(9)
        self.assertEqual(str_val, "09")

        str_val = int_to_string(92)
        self.assertEqual(str_val, "92")

        str_val = int_to_string(10)
        self.assertEqual(str_val, "10")

    def test_serial_number_to_data(self):
        """
        Test case to test serial_number_to_data.
        """

        data = serial_number_to_data(["LEDR", "DATA", "SOFTWARE", "ENGINEER"])
        self.assertListEqual(data, ['LR01', 'DA02', 'SE03', 'ER04'])

        data = serial_number_to_data(["BLUE", "ORANGE", "WHITE"])
        self.assertListEqual(data, ['BE01', 'OE02', 'WE03'])
