from typing import Dict, List
from datetime import datetime, time


class PicoPlacaRule:
    """
    Represents a Pico y Placa restriction rule.
    The Pico y Placa (license plate restriction) rule specifies which vehicles are 
    restricted from driving based on the day of the week, time of day, and the last 
    digit of the license plate number.
    Attributes:
        days_of_week (List[int]): Days of the week when the rule is in effect (0-6, 
                                 where 0 is Monday and 6 is Sunday).
        restricted_digits (List[int]): License plate ending digits that are restricted.
        start_time (time): Starting time for the restriction period.
        end_time (time): Ending time for the restriction period.
    Methods:
        is_restricted(day_of_week, current_time, digit): Determines if a vehicle is 
                                                       restricted based on the rule.
    """

    days_of_week: List[int]
    restricted_digits: List[int]
    start_time: time
    end_time: time
    
    def __init__(self, days_of_week: List[int], restricted_digits: List[int], start_time: time, end_time: time):
        self.days_of_week = days_of_week
        self.restricted_digits = restricted_digits
        self.start_time = start_time
        self.end_time = end_time
    
    def is_restricted(self, day_of_week: int, current_time: time, digit: int) -> bool:
        if day_of_week in self.days_of_week and digit in self.restricted_digits:
            if current_time >= self.start_time and current_time <= self.end_time:
                return True
        return False