# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals
import unittest

from q1c import *


class TestQ1c(unittest.TestCase):

    def test_parenthesis_check(self):
        is_valid = parenthesis_check("[) ()) ()")
        self.assertFalse(is_valid)

        is_valid = parenthesis_check("() {} ()")
        self.assertTrue(is_valid)
