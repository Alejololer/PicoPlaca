from datetime import datetime
from typing import List

from .PicoPlacaRule import PicoPlacaRule


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
        is_vehicle_restricted(datetime, digit): Checks if a vehicle with the given digit is restricted at the specified datetime.
    """

    rules: List[PicoPlacaRule]

    def __init__(self):
        self.rules = []
    
    def add_rule(self, rule: PicoPlacaRule):
        self.rules.append(rule)

    def is_vehicle_restricted(self, datetime: datetime, digit: int) -> bool:
        for rule in self.rules:
            if rule.is_restricted(datetime.weekday(), datetime, digit):
                return True
        return False