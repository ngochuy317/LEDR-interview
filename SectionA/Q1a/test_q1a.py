# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals
import unittest
from unittest.mock import patch

from q1a import *

class TestQ1a(unittest.TestCase):

    def test_convert_str_to_num(self):
        """
        Test case to test convert_str_to_num.
        """

        int_val = convert_str_to_num("13")
        self.assertEqual(int_val, 13)

        int_val = convert_str_to_num("1313")
        self.assertEqual(int_val, 1313)

        int_val = convert_str_to_num("01")
        self.assertEqual(int_val, 1)

        int_val = convert_str_to_num("9999")
        self.assertEqual(int_val, 9999)

    def test_one_digit_to_list_of_word(self):
        """
        Test case to test one_digit_to_list_of_word.
        """

        word = one_digit_to_list_of_word(0)
        self.assertEqual(word, ["Zero"])

        word = one_digit_to_list_of_word(10)
        self.assertEqual(word, ["Ten"])

        word = one_digit_to_list_of_word(19)
        self.assertEqual(word, ["Nineteen"])

        word = one_digit_to_list_of_word(5)
        self.assertEqual(word, ["Five"])

    def test_two_digits_to_list_of_word(self):
        """
        Test case to test test_two_digits_to_list_of_word.
        """

        word = two_digits_to_list_of_word(69)
        self.assertEqual(word, ['Sixty', 'Nine'])

        word = two_digits_to_list_of_word(30)
        self.assertEqual(word, ["Thirty"])

        word = two_digits_to_list_of_word(29)
        self.assertEqual(word, ['Twenty', 'Nine'])

        word = two_digits_to_list_of_word(52)
        self.assertEqual(word, ['Fifty', 'Two'])

    def test_three_digits_to_list_of_word(self):
        """
        Test case to test test_three_digits_to_list_of_word.
        """

        word = three_digits_to_list_of_word(692)
        self.assertEqual(word, ['Six', 'Hundred', 'Ninety', 'Two'])

        word = three_digits_to_list_of_word(310)
        self.assertEqual(word, ['Three', 'Hundred', 'Ten'])

        word = three_digits_to_list_of_word(999)
        self.assertEqual(word, ['Nine', 'Hundred', 'Ninety', 'Nine'])

        word = three_digits_to_list_of_word(521)
        self.assertEqual(word, ['Five', 'Hundred', 'Twenty', 'One'])

    @patch('q1a.three_digits_to_list_of_word')
    @patch('q1a.two_digits_to_list_of_word')
    @patch('q1a.one_digit_to_list_of_word')
    def test_factory_digit_list_of_word(
        self,
        mock_one_digit_to_list_of_word,
        mock_two_digits_to_list_of_word,
        mock_three_digits_to_list_of_word
    ):
        """
        Test case to test factory_digit_list_of_word.
        """
        _ = factory_digit_list_of_word(18)
        mock_one_digit_to_list_of_word.assert_called_with(18)

        _ = factory_digit_list_of_word(51)
        mock_two_digits_to_list_of_word.assert_called_with(51)

        _ = factory_digit_list_of_word(666)
        mock_three_digits_to_list_of_word.assert_called_with(666)


if __name__ == '__main__': 
    unittest.main()
