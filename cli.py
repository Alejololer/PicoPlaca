"""
PicoPlaca CLI Application

Command-line interface for checking vehicle circulation restrictions under Pico y Placa rules.
"""
import argparse
import datetime
from datetime import time

from core.pico_placa_rule import PicoPlacaRule
from core.pico_placa_rule_set import PicoPlacaRuleSet
from core.pico_placa_predictor import PicoPlacaPredictor


def setup_default_rules() -> PicoPlacaRuleSet:
    """
    Sets up the default Pico y Placa rules.
    
    Returns:
        PicoPlacaRuleSet: A rule set configured with the standard Pico y Placa restrictions.
    """
    rule_set = PicoPlacaRuleSet()

    # Morning time window (06:00 to 09:30)
    morning_start = time(6, 0)
    morning_end = time(9, 30)

    # Afternoon time window (16:00 to 20:00)
    afternoon_start = time(16, 0)
    afternoon_end = time(20, 0)

    # Monday: digits 1, 2
    rule_set.add_rule(PicoPlacaRule([0], [1, 2], morning_start, morning_end))
    rule_set.add_rule(PicoPlacaRule([0], [1, 2], afternoon_start, afternoon_end))

    # Tuesday: digits 3, 4
    rule_set.add_rule(PicoPlacaRule([1], [3, 4], morning_start, morning_end))
    rule_set.add_rule(PicoPlacaRule([1], [3, 4], afternoon_start, afternoon_end))

    # Wednesday: digits 5, 6
    rule_set.add_rule(PicoPlacaRule([2], [5, 6], morning_start, morning_end))
    rule_set.add_rule(PicoPlacaRule([2], [5, 6], afternoon_start, afternoon_end))

    # Thursday: digits 7, 8
    rule_set.add_rule(PicoPlacaRule([3], [7, 8], morning_start, morning_end))
    rule_set.add_rule(PicoPlacaRule([3], [7, 8], afternoon_start, afternoon_end))

    # Friday: digits 9, 0
    rule_set.add_rule(PicoPlacaRule([4], [9, 0], morning_start, morning_end))
    rule_set.add_rule(PicoPlacaRule([4], [9, 0], afternoon_start, afternoon_end))

    return rule_set


def parse_arguments():
    """
    Parse command line arguments.
    
    Returns:
        argparse.Namespace: An object containing the parsed arguments.
    """
    parser = argparse.ArgumentParser(
        description='Check if a vehicle is restricted from circulation'+
        'according to Pico y Placa rules.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        '-p', '--plate', 
        required=True,
        help='The license plate number in format XXX-#### or XXX-###'
    )

    parser.add_argument(
        '-d', '--date',
        default=datetime.date.today().isoformat(),
        help='The date to check in format YYYY-MM-DD (defaults to today)'
    )

    parser.add_argument(
        '-t', '--time',
        default=datetime.datetime.now().strftime('%H:%M'),
        help='The time to check in format HH:MM (defaults to current time)'
    )

    return parser.parse_args()


def main():
    """
    Main entry point for the CLI application.
    """
    args = parse_arguments()

    # Set up the rules
    rule_set = setup_default_rules()

    # Create the predictor
    predictor = PicoPlacaPredictor(rule_set)

    # Predict restriction
    result = predictor.predict_restriction(args.plate, args.date, args.time)

    # Display the result
    print(result)


if __name__ == "__main__":
    main()
