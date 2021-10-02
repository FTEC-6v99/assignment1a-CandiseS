# Create a unit test method to test the calculate_avg function created in the utils module
# Make sure you include multiple unit tests to test that the function acts as expected in different scenarios

import unittest
from app.src.utils import calc_avg

class Utiltest(unittest.TestCase):

     def test_cal_avg(self) :
        numbers = [5, 5, 5, 5]
        expected_num = 5
        actual_num = calc_avg(numbers)
        self.assertEquals(expected_num, actual_num)
