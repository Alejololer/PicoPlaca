from datetime import datetime
from typing import Optional

from .PicoPlacaRuleSet import PicoPlacaRuleSet


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
        return self.rule_set.is_vehicle_restricted(dt, last_digit)
