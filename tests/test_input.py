"""
Test module for the input parser classes.
This module contains unit tests that verify the functionality of the DateTimeParser
and LicensePlateParser classes, ensuring they correctly parse and validate input data.
"""
import unittest
from input import DateTimeParser, LicensePlateParser

class TestDateTimeParser(unittest.TestCase):
    """Test cases for the DateTimeParser class."""

    def test_parse_datetime(self):
        """Test that parse_datetime correctly parses valid date and time strings."""
        datetime = DateTimeParser.parse_datetime("2021-09-01", "08:00")
        self.assertEqual(datetime.year, 2021)
        self.assertEqual(datetime.month, 9)
        self.assertEqual(datetime.day, 1)
        self.assertEqual(datetime.hour, 8)
        self.assertEqual(datetime.minute, 0)

    def test_parse_datetime_invalid_format(self):
        """Test that parse_datetime raises ValueError for invalid time format."""
        with self.assertRaises(ValueError):
            DateTimeParser.parse_datetime("2021-09-01", "")

class TestLicensePlateParser(unittest.TestCase):
    """Test cases for the LicensePlateParser class."""

    def test_parse_license_plate(self):
        """Test that parse_license_plate correctly extracts the last digit 
        from a valid license plate."""
        digit = LicensePlateParser.parse_license_plate("ABC-123")
        self.assertEqual(digit, 3)

    def test_parse_license_plate_invalid(self):
        """Test that parse_license_plate raises ValueError for invalid license plate formats."""
        with self.assertRaises(ValueError):
            LicensePlateParser.parse_license_plate("ABC-12")
        with self.assertRaises(ValueError):
            LicensePlateParser.parse_license_plate("AB-1234")
        with self.assertRaises(ValueError):
            LicensePlateParser.parse_license_plate("ABC-1B34")


if __name__ == '__main__':
    unittest.main()
