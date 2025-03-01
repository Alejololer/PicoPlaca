"""
PicoPlacaPredictor Module

This module provides functionality to predict 'Pico y Placa' driving restrictions.
'Pico y Placa' (Peak and Plate) is a traffic restriction policy implemented in various
cities, particularly in Latin America, to reduce traffic congestion during peak hours.
Vehicles are restricted from circulation based on the last digit of their license plates
on specific days and times.

This module contains the PicoPlacaPredictor class which evaluates whether a vehicle
with a given license plate is restricted from circulation at a specific date and time
according to a defined rule set.
"""

from datetime import datetime
from .pico_placa_rule_set import PicoPlacaRuleSet


class PicoPlacaPredictor:
    """
    A class to predict whether a vehicle has a restriction according to the 'Pico y Placa' rules.
    This class evaluates if a license plate has a circulation restriction based on
    the given date and time according to a specific rule set.
    Attributes:
        rule_set (PicoPlacaRuleSet): The rule set that defines the restrictions.
    Methods:
        predict_restriction(license_plate, dt): Determines if a vehicle is restricted.
    """

    rule_set: PicoPlacaRuleSet

    def __init__(self, rule_set: PicoPlacaRuleSet):
        self.rule_set = rule_set

    def predict_restriction(self, last_digit: int, dt: datetime) -> bool:
        """
        Predicts if a vehicle with the given last digit is restricted at the specified datetime.
        This method applies the current rule set to determine if a vehicle with the provided
        license plate's last digit has driving restrictions at the given date and time.
        Args:
        last_digit : int
            The last digit of the vehicle's license plate.
        dt : datetime
            The date and time to check for restrictions.
        Returns:
        bool
            True if the vehicle is restricted from driving at the specified time,
            False otherwise.
        """

        return self.rule_set.is_vehicle_restricted(dt, last_digit)
