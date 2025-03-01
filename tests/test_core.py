import unittest
from datetime import time
from core import PicoPlacaRule

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
        
if __name__ == '__main__':
    unittest.main()