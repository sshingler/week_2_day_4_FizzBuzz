import unittest

from src.FizzBuzz import *

class TestFizzBuzz(unittest.TestCase):

        def test_has_input(self):
            self.assertEqual(6, fizz_buzz(6))

        def test_compare_num1__divides_3(self):
            self.assertEqual("fizz", divide_3(6))

        def test_compare_num1__does_not_divides_3(self):
            self.assertEqual("7 is not divisibile by 3", divide_3(7))

        def test_compare_num1__divides_5(self):
            self.assertEqual("buzz", divide_5(10))

        def test_compare_num1__does_not_divides_5(self):
            self.assertEqual("7 is not divisible by 5", divide_5(7))

        def test_divides_by_3_and_5(self):
            self.assertEqual("fizzbuzz", divide_by_3_and_5(15))

        def test_does_not_divide_by_3_and_5(self):
            self.assertEqual("2", divide_by_3_and_5(2)) 


        def test_fizz_buzz_game(self):
            self.assertEqual("fizzbuzz", fizz_buzz_game(15))
            self.assertEqual("fizz", fizz_buzz_game(3))
            self.assertEqual("buzz", fizz_buzz_game(5))
            self.assertEqual("11", fizz_buzz_game(11))
            



