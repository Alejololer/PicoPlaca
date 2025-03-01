import unittest
from datetime import time
from core import PicoPlacaRule
from input import DateTimeParser

class TestPicoPlacaRule(unittest.TestCase):

    def test_is_restricted_within_window(self):
        rule = PicoPlacaRule([0,1,2], [1], time(7,0), time(9,30))
        self.assertTrue(rule.is_restricted(0, time(7,0), 1))
        self.assertTrue(rule.is_restricted(0, time(9,30), 1))
        self.assertTrue(rule.is_restricted(0, time(8,0), 1))
    
    def test_is_not_restricted_outside_window(self):
        rule = PicoPlacaRule([0,1,2], [1], time(7,0), time(9,30))
        self.assertFalse(rule.is_restricted(0, time(6,59), 1))
        self.assertFalse(rule.is_restricted(0, time(9,31), 1))
        self.assertFalse(rule.is_restricted(0, time(10,0), 1))
    
    def test_is_restricted_at_boundary(self):
        rule = PicoPlacaRule([0,1,2], [1], time(7,0), time(9,30))
        self.assertTrue(rule.is_restricted(0, time(7,0), 1))
        self.assertTrue(rule.is_restricted(0, time(9,30), 1))
    
    def test_is_not_restricted_different_day(self):
        rule = PicoPlacaRule([0,1,2], [1], time(7,0), time(9,30))
        self.assertFalse(rule.is_restricted(3, time(7,0), 1))
        self.assertFalse(rule.is_restricted(3, time(9,30), 1))
        self.assertFalse(rule.is_restricted(3, time(8,0), 1))
    
    def test_is_not_restricted_different_digit(self):
        rule = PicoPlacaRule([0,1,2], [1], time(7,0), time(9,30))
        self.assertFalse(rule.is_restricted(0, time(7,0), 2))
        self.assertFalse(rule.is_restricted(0, time(9,30), 2))
        self.assertFalse(rule.is_restricted(0, time(8,0), 2))

class TestDateTimeParser(unittest.TestCase):

    def test_parse_datetime(self):
        datetime = DateTimeParser.parse_datetime("2021-09-01 08:00")
        self.assertEqual(datetime.year, 2021)
        self.assertEqual(datetime.month, 9)
        self.assertEqual(datetime.day, 1)
        self.assertEqual(datetime.hour, 8)
        self.assertEqual(datetime.minute, 0)
    
    def test_parse_datetime_invalid_format(self):
        with self.assertRaises(ValueError):
            DateTimeParser.parse_datetime("2021-09-01")
        
if __name__ == '__main__':
    unittest.main()