import pytest
import unittest2

from operatorsii import *
class Num_calc(unittest2.TestCase):

    casio = Calctest()

    def test_addition(self):
        self.assertEqual(self.casio.addition(9, 1), 10)

    def test_subtraction(self):
        self.assertEqual(self.casio.subtraction(9, 2), 7)

    def test_division(self):
        self.assertEqual(self.casio.division(10, 2), 5)

    def test_multiply(self):
        self.assertEqual(self.casio.multiply(9, 2), 18)
