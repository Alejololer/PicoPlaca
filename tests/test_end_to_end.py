"""
End-to-End tests for the Pico y Placa system.

Contains comprehensive tests that verify the complete system functionality using real components.
"""
import unittest
from datetime import time
from core import PicoPlacaRule, PicoPlacaRuleSet, PicoPlacaPredictor


class TestPicoPlacaPredictorEndToEnd(unittest.TestCase):
    """Test cases for end-to-end validation of the PicoPlacaPredictor."""

    # Constants for expected messages
    RESTRICTED_MSG = "Vehicle is restricted to circulate at this time and date"
    NOT_RESTRICTED_MSG = "Vehicle is not restricted to circulate at this time and date"

    # Error message constants
    ERROR_PREFIX = "Error: "
    LICENSE_PLATE_ERROR_PREFIX = "Error: Invalid license plate format: '"
    LICENSE_PLATE_ERROR_FORMAT = "Expected format: 'XXX-###' or 'XXX-####'"
    DATETIME_ERROR_PREFIX = "Error: Unable to parse '"
    DATETIME_ERROR_FORMAT = "Expected format: 'YYYY-MM-DD HH:MM'"
    NO_RULES_ERROR_PREFIX = "Error: No Pico y Placa rules are defined in the ruleset"

    def setUp(self):
        """Set up test fixtures with real rules for Quito's Pico y Placa system."""
        self.rule_set = PicoPlacaRuleSet()

        # Monday restrictions (plate numbers 1 and 2)
        self.rule_set.add_rule(PicoPlacaRule(days_of_week=[0], restricted_digits=[1, 2],
                                              start_time=time(6, 0), end_time=time(9, 30)))
        self.rule_set.add_rule(PicoPlacaRule(days_of_week=[0], restricted_digits=[1, 2],
                                              start_time=time(16, 0), end_time=time(20, 0)))

        # Tuesday restrictions (plate numbers 3 and 4)
        self.rule_set.add_rule(PicoPlacaRule(days_of_week=[1], restricted_digits=[3, 4],
                                              start_time=time(6, 0), end_time=time(9, 30)))
        self.rule_set.add_rule(PicoPlacaRule(days_of_week=[1], restricted_digits=[3, 4],
                                              start_time=time(16, 0), end_time=time(20, 0)))

        # Wednesday restrictions (plate numbers 5 and 6)
        self.rule_set.add_rule(PicoPlacaRule(days_of_week=[2], restricted_digits=[5, 6],
                                              start_time=time(6, 0), end_time=time(9, 30)))
        self.rule_set.add_rule(PicoPlacaRule(days_of_week=[2], restricted_digits=[5, 6],
                                              start_time=time(16, 0), end_time=time(20, 0)))

        # Thursday restrictions (plate numbers 7 and 8)
        self.rule_set.add_rule(PicoPlacaRule(days_of_week=[3], restricted_digits=[7, 8],
                                              start_time=time(6, 0), end_time=time(9, 30)))
        self.rule_set.add_rule(PicoPlacaRule(days_of_week=[3], restricted_digits=[7, 8],
                                              start_time=time(16, 0), end_time=time(20, 0)))

        # Friday restrictions (plate numbers 9 and 0)
        self.rule_set.add_rule(PicoPlacaRule(days_of_week=[4], restricted_digits=[9, 0],
                                              start_time=time(6, 0), end_time=time(9, 30)))
        self.rule_set.add_rule(PicoPlacaRule(days_of_week=[4], restricted_digits=[9, 0],
                                              start_time=time(16, 0), end_time=time(20, 0)))

        # Create the predictor with the rule set
        self.predictor = PicoPlacaPredictor(self.rule_set)

    def test_restricted_vehicle(self):
        """Test a vehicle that should be restricted."""
        # Monday morning with last digit 1
        result = self.predictor.predict_restriction("ABC-121", "2023-10-02", "08:00")
        self.assertEqual(result, self.RESTRICTED_MSG)

        # Friday afternoon with last digit 0
        result = self.predictor.predict_restriction("XYZ-100", "2023-10-06", "17:30")
        self.assertEqual(result, self.RESTRICTED_MSG)

    def test_unrestricted_vehicle_different_digit(self):
        """Test a vehicle that should not be restricted due to different last digit."""
        # Monday morning with last digit 3 (not restricted on Monday)
        result = self.predictor.predict_restriction("ABC-123", "2023-10-02", "08:00")
        self.assertEqual(result, self.NOT_RESTRICTED_MSG)

    def test_unrestricted_vehicle_outside_time_window(self):
        """Test a vehicle that should not be restricted because outside time window."""
        # Monday late morning (after restriction) with last digit 1
        result = self.predictor.predict_restriction("ABC-121", "2023-10-02", "10:00")
        self.assertEqual(result, self.NOT_RESTRICTED_MSG)

        # Monday early afternoon (before restriction) with last digit 1
        result = self.predictor.predict_restriction("ABC-121", "2023-10-02", "15:00")
        self.assertEqual(result, self.NOT_RESTRICTED_MSG)

    def test_unrestricted_weekend(self):
        """Test a vehicle on weekend (should not be restricted)."""
        # Saturday with last digit 1
        result = self.predictor.predict_restriction("ABC-121", "2023-10-07", "08:00")
        self.assertEqual(result, self.NOT_RESTRICTED_MSG)

        # Sunday with last digit 0
        result = self.predictor.predict_restriction("XYZ-100", "2023-10-08", "17:30")
        self.assertEqual(result, self.NOT_RESTRICTED_MSG)

    def test_invalid_license_plate(self):
        """Test an invalid license plate format."""
        result = self.predictor.predict_restriction("INVALID", "2023-10-02", "08:00")
        self.assertTrue(result.startswith(self.LICENSE_PLATE_ERROR_PREFIX))
        self.assertTrue(self.LICENSE_PLATE_ERROR_FORMAT in result)

        result = self.predictor.predict_restriction("123-ABC", "2023-10-02", "08:00")
        self.assertTrue(result.startswith(self.LICENSE_PLATE_ERROR_PREFIX))
        self.assertTrue(self.LICENSE_PLATE_ERROR_FORMAT in result)

    def test_invalid_date_time(self):
        """Test invalid date and time formats."""
        result = self.predictor.predict_restriction("ABC-123", "2023/10/02", "08:00")
        self.assertTrue(result.startswith(self.DATETIME_ERROR_PREFIX))
        self.assertTrue(self.DATETIME_ERROR_FORMAT in result)

        result = self.predictor.predict_restriction("ABC-123", "2023-10-02", "8:00am")
        self.assertTrue(result.startswith(self.DATETIME_ERROR_PREFIX))
        self.assertTrue(self.DATETIME_ERROR_FORMAT in result)

    def test_no_rules_defined(self):
        """Test the behavior when no rules are defined."""
        # Create a new empty ruleset and predictor
        empty_rule_set = PicoPlacaRuleSet()
        empty_predictor = PicoPlacaPredictor(empty_rule_set)

        # Test prediction with no rules
        result = empty_predictor.predict_restriction("ABC-123", "2023-10-02", "08:00")
        self.assertTrue(result.startswith(self.NO_RULES_ERROR_PREFIX))

    def test_boundary_conditions(self):
        """Test edge cases at the boundaries of restriction windows."""
        # Test start of morning restriction (6:00 AM)
        result = self.predictor.predict_restriction("ABC-121", "2023-10-02", "06:00")
        self.assertEqual(result, self.RESTRICTED_MSG)

        # Test just before morning restriction (5:59 AM)
        result = self.predictor.predict_restriction("ABC-121", "2023-10-02", "05:59")
        self.assertEqual(result, self.NOT_RESTRICTED_MSG)

        # Test end of morning restriction (9:30 AM - exclusive)
        result = self.predictor.predict_restriction("ABC-121", "2023-10-02", "09:30")
        self.assertEqual(result, self.NOT_RESTRICTED_MSG)

        # Test just before end of morning restriction (9:29 AM)
        result = self.predictor.predict_restriction("ABC-121", "2023-10-02", "09:29")
        self.assertEqual(result, self.RESTRICTED_MSG)

        # Test start of afternoon restriction (16:00)
        result = self.predictor.predict_restriction("ABC-121", "2023-10-02", "16:00")
        self.assertEqual(result, self.RESTRICTED_MSG)

        # Test just before afternoon restriction (15:59)
        result = self.predictor.predict_restriction("ABC-121", "2023-10-02", "15:59")
        self.assertEqual(result, self.NOT_RESTRICTED_MSG)

        # Test end of afternoon restriction (20:00 - exclusive)
        result = self.predictor.predict_restriction("ABC-121", "2023-10-02", "20:00")
        self.assertEqual(result, self.NOT_RESTRICTED_MSG)

        # Test just before end of afternoon restriction (19:59)
        result = self.predictor.predict_restriction("ABC-121", "2023-10-02", "19:59")
        self.assertEqual(result, self.RESTRICTED_MSG)


if __name__ == '__main__':
    unittest.main()
