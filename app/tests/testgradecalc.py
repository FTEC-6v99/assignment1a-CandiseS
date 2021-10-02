# Use unittest library to create a unit test method to test the calculate_avg_grade function created in the gradecalc module
# Make sure you include multiple unit tests to test that the function acts as expected in different scenarios
import unittest
from app.src.Student import Student
from app.src.gradecalc import calc_avg_grade
class GradeCaltest(unittest.TestCase):
    def test_cal_grade(self):
        input = [
            Student('candise', 20, 1824, 80), Student('candise', 20, 1824, 100), Student('emily', 25, 1850, 90)
        ]

        expected = {1824: 90, 1850: 90}

        actual = calc_avg_grade(input)
        self.assertEquals(expected, actual)