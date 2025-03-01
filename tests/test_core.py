"""
Test module for the PicoPlacaRule class.
This module contains unit tests that verify the functionality of the PicoPlacaRule class,
ensuring it correctly determines vehicle restrictions based on day, time, and license plate digit.
"""
import unittest
from datetime import time, datetime
from unittest.mock import patch
from core import PicoPlacaRule, PicoPlacaRuleSet, PicoPlacaPredictor
from core.pico_placa_rule_set import NoRulesDefinedError

class TestPicoPlacaRule(unittest.TestCase):
    """Test cases for the PicoPlacaRule class."""

    def test_is_restricted_within_window(self):
        """Test that is_restricted returns True when all restriction conditions are met."""
        rule = PicoPlacaRule([0,1,2], [1], time(7,0), time(9,30))
        self.assertTrue(rule.is_restricted(0, time(7,0), 1))
        # Right edge should be exclusive, so time(9,30) should not be restricted
        self.assertFalse(rule.is_restricted(0, time(9,30), 1))
        self.assertTrue(rule.is_restricted(0, time(8,0), 1))

    def test_is_not_restricted_outside_window(self):
        """Test that is_restricted returns False when the time is outside the restriction window."""
        rule = PicoPlacaRule([0,1,2], [1], time(7,0), time(9,30))
        self.assertFalse(rule.is_restricted(0, time(6,59), 1))
        self.assertFalse(rule.is_restricted(0, time(9,31), 1))
        self.assertFalse(rule.is_restricted(0, time(10,0), 1))

    def test_is_restricted_at_boundary(self):
        """Test that is_restricted returns True for the left boundary (inclusive) 
        and False for the right boundary (exclusive)."""
        rule = PicoPlacaRule([0,1,2], [1], time(7,0), time(9,30))
        self.assertTrue(rule.is_restricted(0, time(7,0), 1))  # Left edge is inclusive
        self.assertFalse(rule.is_restricted(0, time(9,30), 1))  # Right edge is exclusive

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

class TestPicoPlacaRuleSet(unittest.TestCase):
    """Test cases for the PicoPlacaRuleSet class."""

    def setUp(self):
        """Set up test fixtures."""
        self.rule_set = PicoPlacaRuleSet()
        self.monday_rule = PicoPlacaRule([0], [1, 2], time(7, 0), time(9, 30))
        self.tuesday_rule = PicoPlacaRule([1], [3, 4], time(7, 0), time(9, 30))

    def test_add_rule(self):
        """Test that rules are properly added to the rule set."""
        self.rule_set.add_rule(self.monday_rule)
        self.assertEqual(len(self.rule_set.rules_by_day[0]), 1)
        self.assertEqual(len(self.rule_set.rules_by_day[1]), 0)

        self.rule_set.add_rule(self.tuesday_rule)
        self.assertEqual(len(self.rule_set.rules_by_day[0]), 1)
        self.assertEqual(len(self.rule_set.rules_by_day[1]), 1)

    def test_has_rules(self):
        """Test that has_rules correctly identifies when rules are present."""
        self.assertFalse(self.rule_set.has_rules())

        self.rule_set.add_rule(self.monday_rule)
        self.assertTrue(self.rule_set.has_rules())

    def test_is_vehicle_restricted(self):
        """Test that vehicle restrictions are correctly identified."""
        self.rule_set.add_rule(self.monday_rule)

        # Monday at 8:00 with digit 1 should be restricted
        monday_datetime = datetime(2023, 10, 2, 8, 0)  # A Monday
        self.assertTrue(self.rule_set.is_vehicle_restricted(monday_datetime, 1))

        # Monday at 8:00 with digit 5 should not be restricted
        self.assertFalse(self.rule_set.is_vehicle_restricted(monday_datetime, 5))

        # Tuesday at 8:00 with digit 1 should not be restricted
        tuesday_datetime = datetime(2023, 10, 3, 8, 0)  # A Tuesday
        self.assertFalse(self.rule_set.is_vehicle_restricted(tuesday_datetime, 1))

        # Add Tuesday rule and test
        self.rule_set.add_rule(self.tuesday_rule)
        self.assertTrue(self.rule_set.is_vehicle_restricted(tuesday_datetime, 3))
        self.assertFalse(self.rule_set.is_vehicle_restricted(tuesday_datetime, 5))

    def test_no_rules_defined_error(self):
        """Test that NoRulesDefinedError is raised when appropriate."""
        test_datetime = datetime(2023, 10, 2, 8, 0)

        # Should raise error when no rules defined and raise_on_no_rules=True
        with self.assertRaises(NoRulesDefinedError):
            self.rule_set.is_vehicle_restricted(test_datetime, 1)

        # Should return False when no rules defined and raise_on_no_rules=False
        self.assertFalse(self.rule_set.is_vehicle_restricted(
            test_datetime, 1, raise_on_no_rules=False))


class TestPicoPlacaPredictor(unittest.TestCase):
    """Test cases for the PicoPlacaPredictor class."""

    def setUp(self):
        """Set up test fixtures."""
        self.rule_set = PicoPlacaRuleSet()
        self.monday_rule = PicoPlacaRule([0], [1, 2], time(7, 0), time(9, 30))
        self.rule_set.add_rule(self.monday_rule)
        self.predictor = PicoPlacaPredictor(self.rule_set)

    @patch('input.LicensePlateParser.parse_license_plate')
    @patch('input.DateTimeParser.parse_datetime')
    @patch('output.OutputFormatter.format_prediction')
    def test_predict_restriction_restricted(self, mock_format, mock_parse_datetime,
                                            mock_parse_license):
        """Test prediction when vehicle is restricted."""
        # Setup mocks
        mock_parse_license.return_value = 1  # License plate ends with 1
        mock_parse_datetime.return_value = datetime(2023, 10, 2, 8, 0)  # A Monday at 8:00
        mock_format.return_value = "Vehicle is restricted"

        result = self.predictor.predict_restriction("ABC-123", "2023-10-02", "08:00")

        mock_parse_license.assert_called_once_with("ABC-123")
        mock_parse_datetime.assert_called_once_with("2023-10-02", "08:00")
        mock_format.assert_called_once_with(True)
        self.assertEqual(result, "Vehicle is restricted")

    @patch('input.LicensePlateParser.parse_license_plate')
    @patch('input.DateTimeParser.parse_datetime')
    @patch('output.OutputFormatter.format_prediction')
    def test_predict_restriction_not_restricted(self, mock_format, mock_parse_datetime,
                                                mock_parse_license):
        """Test prediction when vehicle is not restricted."""
        # Setup mocks
        mock_parse_license.return_value = 5  # License plate ends with 5
        mock_parse_datetime.return_value = datetime(2023, 10, 2, 8, 0)  # A Monday at 8:00
        mock_format.return_value = "Vehicle is not restricted"

        result = self.predictor.predict_restriction("ABC-125", "2023-10-02", "08:00")

        mock_parse_license.assert_called_once_with("ABC-125")
        mock_parse_datetime.assert_called_once_with("2023-10-02", "08:00")
        mock_format.assert_called_once_with(False)
        self.assertEqual(result, "Vehicle is not restricted")

    @patch('input.LicensePlateParser.parse_license_plate')
    def test_predict_restriction_invalid_license(self, mock_parse_license):
        """Test prediction with invalid license plate."""
        # Setup mock to raise error
        mock_parse_license.side_effect = ValueError("Invalid license plate")

        result = self.predictor.predict_restriction("INVALID", "2023-10-02", "08:00")

        mock_parse_license.assert_called_once_with("INVALID")
        self.assertEqual(result, "Error: Invalid license plate")

    @patch('input.LicensePlateParser.parse_license_plate')
    @patch('input.DateTimeParser.parse_datetime')
    def test_predict_restriction_invalid_datetime(self, mock_parse_datetime, mock_parse_license):
        """Test prediction with invalid datetime."""
        # Setup mocks
        mock_parse_license.return_value = 1
        mock_parse_datetime.side_effect = ValueError("Invalid date or time format")

        result = self.predictor.predict_restriction("ABC-123", "invalid-date", "08:00")

        mock_parse_license.assert_called_once_with("ABC-123")
        mock_parse_datetime.assert_called_once_with("invalid-date", "08:00")
        self.assertEqual(result, "Error: Invalid date or time format")


if __name__ == '__main__':
    unittest.main()
