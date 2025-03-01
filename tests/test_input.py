import unittest
from input import DateTimeParser, LicensePlateParser

class TestDateTimeParser(unittest.TestCase):

    def test_parse_datetime(self):
        datetime = DateTimeParser.parse_datetime("2021-09-01", "08:00")
        self.assertEqual(datetime.year, 2021)
        self.assertEqual(datetime.month, 9)
        self.assertEqual(datetime.day, 1)
        self.assertEqual(datetime.hour, 8)
        self.assertEqual(datetime.minute, 0)
    
    def test_parse_datetime_invalid_format(self):
        with self.assertRaises(ValueError):
            DateTimeParser.parse_datetime("2021-09-01", "")

class TestLicensePlateParser(unittest.TestCase):
    
    def test_parse_license_plate(self):
        digit = LicensePlateParser.parse_license_plate("ABC-123")
        self.assertEqual(digit, 3)
    
    def test_parse_license_plate_invalid(self):
        with self.assertRaises(ValueError):
            LicensePlateParser.parse_license_plate("ABC-12")
        with self.assertRaises(ValueError):
            LicensePlateParser.parse_license_plate("AB-1234")
        with self.assertRaises(ValueError):
            LicensePlateParser.parse_license_plate("ABC-1B34")


if __name__ == '__main__':
    unittest.main()