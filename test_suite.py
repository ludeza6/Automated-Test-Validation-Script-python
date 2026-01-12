import unittest
from test_validator import Measurement

class TestMeasurementValidation(unittest.TestCase):
    def test_pass_condition(self):
        m = Measurement("Test", 5.0, 4.0, 6.0, "V")
        self.assertTrue(m.passed)

    def test_fail_condition(self):
        m = Measurement("Test", 3.0, 4.0, 6.0, "V")
        self.assertFalse(m.passed)

if __name__ == '__main__':
    unittest.main()