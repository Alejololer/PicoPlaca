import unittest
from output import OutputFormatter

class TestOutputFormatter(unittest.TestCase):

    def test_format_output_restricted(self):
        message = OutputFormatter.format_prediction(True)
        self.assertEqual(message, "Vehicle is restricted to circulate at this time and date")

    def test_format_output_not_restricted(self):
        message = OutputFormatter.format_prediction(False)
        self.assertEqual(message, "Vehicle is not restricted to circulate at this time and date")

if __name__ == '__main__':
    unittest.main()