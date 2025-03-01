"""
Test module for the PicoPlacaRule class.
This module contains unit tests that verify the functionality of the PicoPlacaRule class,
ensuring it correctly determines vehicle restrictions based on day, time, and license plate digit.
"""
import unittest
from datetime import time
from core import PicoPlacaRule

class TestPicoPlacaRule(unittest.TestCase):
    """Test cases for the PicoPlacaRule class."""

    def test_is_restricted_within_window(self):
        """Test that is_restricted returns True when all restriction conditions are met."""
        rule = PicoPlacaRule([0,1,2], [1], time(7,0), time(9,30))
        self.assertTrue(rule.is_restricted(0, time(7,0), 1))
        self.assertTrue(rule.is_restricted(0, time(9,30), 1))
        self.assertTrue(rule.is_restricted(0, time(8,0), 1))

    def test_is_not_restricted_outside_window(self):
        """Test that is_restricted returns False when the time is outside the restriction window."""
        rule = PicoPlacaRule([0,1,2], [1], time(7,0), time(9,30))
        self.assertFalse(rule.is_restricted(0, time(6,59), 1))
        self.assertFalse(rule.is_restricted(0, time(9,31), 1))
        self.assertFalse(rule.is_restricted(0, time(10,0), 1))

    def test_is_restricted_at_boundary(self):
        """Test that is_restricted returns True when the time is at the boundary of 
        the restriction window."""
        rule = PicoPlacaRule([0,1,2], [1], time(7,0), time(9,30))
        self.assertTrue(rule.is_restricted(0, time(7,0), 1))
        self.assertTrue(rule.is_restricted(0, time(9,30), 1))

    def test_is_not_restricted_different_day(self):
        """Test that is_restricted returns False when the day is not restricted."""
        rule = PicoPlacaRule([0,1,2], [1], time(7,0), time(9,30))
        self.assertFalse(rule.is_restricted(3, time(7,0), 1))
        self.assertFalse(rule.is_restricted(3, time(9,30), 1))
        self.assertFalse(rule.is_restricted(3, time(8,0), 1))

    def test_is_not_restricted_different_digit(self):
        """Test that is_restricted returns False when the license plate digit is not restricted."""
        rule = PicoPlacaRule([0,1,2], [1], time(7,0), time(9,30))
        self.assertFalse(rule.is_restricted(0, time(7,0), 2))
        self.assertFalse(rule.is_restricted(0, time(9,30), 2))
        self.assertFalse(rule.is_restricted(0, time(8,0), 2))

if __name__ == '__main__':
    unittest.main()
