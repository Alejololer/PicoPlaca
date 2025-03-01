from datetime import datetime
from typing import List

from .PicoPlacaRule import PicoPlacaRule


class NoRulesDefinedError(Exception):
    """Exception raised when attempting to check restrictions with no rules defined."""
    pass


class PicoPlacaRuleSet:
    """
    PicoPlacaRuleSet is a class that manages a collection of pico y placa rules.
    This class allows adding rules and checking whether a vehicle with a specific 
    last digit in its license plate is restricted from circulation at a given datetime.
    Attributes:
        rules (List[PicoPlacaRule]): A list of PicoPlacaRule objects.
    Methods:
        __init__(): Initializes an empty list of rules.
        add_rule(rule): Adds a rule to the rule set.
        has_rules(): Checks if any rules are defined.
        is_vehicle_restricted(datetime, digit): Checks if a vehicle with the given digit is restricted at the specified datetime.
    """

    rules: List[PicoPlacaRule]

    def __init__(self):
        self.rules = []
    
    def add_rule(self, rule: PicoPlacaRule):
        self.rules.append(rule)

    def has_rules(self) -> bool:
        return len(self.rules) > 0

    def is_vehicle_restricted(self, datetime: datetime, digit: int, raise_on_no_rules: bool = True) -> bool:
        if not self.has_rules():
            if raise_on_no_rules:
                raise NoRulesDefinedError("No Pico y Placa rules are defined in the ruleset.")
            return False
            
        for rule in self.rules:
            if rule.is_restricted(datetime.weekday(), datetime, digit):
                return True
        return False