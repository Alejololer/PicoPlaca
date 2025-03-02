"""
PicoPlacaPredictor Module

Evaluates vehicle circulation restrictions based on license plates, dates, and times.
"""

from input import LicensePlateParser, DateTimeParser
from output import OutputFormatter
from .pico_placa_rule_set import PicoPlacaRuleSet, NoRulesDefinedError


class PicoPlacaPredictor:
    """
    A class that predicts driving restrictions according to 'Pico y Placa' rules.
    
    This class determines if a vehicle is restricted from circulation based on
    its license plate, date, and time, according to a specific rule set.
    
    Attributes:
        rule_set (PicoPlacaRuleSet): The rule set defining the restriction parameters
            including restricted days, times, and license plate digits.
    """

    rule_set: PicoPlacaRuleSet

    def __init__(self, rule_set: PicoPlacaRuleSet):
        self.rule_set = rule_set

    def predict_restriction(self, license_plate: str, date: str, time: str) -> str:
        """
        Predicts if a vehicle with the given license plate is restricted at the 
        specified date and time.
        
        This method extracts the last digit from the license plate and evaluates it against
        the current rule set to determine if driving restrictions apply at the given date and time.
        
        Args:
            license_plate (str): The vehicle's license plate to check.
            date (str): The date to check in an acceptable format 
            (will be parsed by DateTimeParser).
            time (str): The time to check in an acceptable format 
            (will be parsed by DateTimeParser).
            
        Returns:
            str: A formatted message indicating whether the vehicle is restricted or not,
                 or an error message if input validation fails or an unexpected error occurs.
        """
        try:
            last_digit = LicensePlateParser.parse_license_plate(license_plate)
            date_time = DateTimeParser.parse_datetime(date, time)
            restricted = self.rule_set.is_vehicle_restricted(date_time, last_digit)
            return OutputFormatter.format_prediction(restricted)
        except ValueError as e:
            return f"Error: {str(e)}"
        except NoRulesDefinedError as e:
            return f"Error: {str(e)}"
