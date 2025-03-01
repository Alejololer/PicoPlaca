"""
Test module for the OutputFormatter class.
This module contains unit tests that verify the functionality of the OutputFormatter class,
ensuring it correctly formats prediction results into human-readable messages.
"""
import unittest
from output import OutputFormatter

class TestOutputFormatter(unittest.TestCase):
    """Test cases for the OutputFormatter class."""

    def test_format_output_restricted(self):
        """Test that format_prediction returns the correct message when a vehicle is restricted."""
        message = OutputFormatter.format_prediction(True)
        self.assertEqual(message, "Vehicle is restricted to circulate at this time and date")

    def test_format_output_not_restricted(self):
        """Test that format_prediction returns the correct message when a vehicle
          is not restricted."""
        message = OutputFormatter.format_prediction(False)
        self.assertEqual(message, "Vehicle is not restricted to circulate at this time and date")

if __name__ == '__main__':
    unittest.main()
