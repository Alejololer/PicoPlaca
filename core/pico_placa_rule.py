"""
Pico y Placa Rule Module

This module defines the PicoPlacaRule class which represents a single rule in the 
Pico y Placa system. Each rule specifies which vehicles are restricted from driving 
based on the day of the week, time of day, and the last digit of the license plate number.

The Pico y Placa system aims to reduce traffic congestion during peak hours by restricting
vehicle circulation based on these parameters.
"""
from typing import List
from datetime import time


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

    def __init__(self, days_of_week: List[int], restricted_digits: List[int],
                  start_time: time, end_time: time):
        self.days_of_week = days_of_week
        self.restricted_digits = restricted_digits
        self.start_time = start_time
        self.end_time = end_time

    def is_restricted(self, day_of_week: int, current_time: time, digit: int) -> bool:
        """
        Determines whether a vehicle is restricted from circulation based on Pico y Placa rules.
        Args:
            day_of_week (int): Day of the week (0 = Monday, 1 = Tuesday, ..., 6 = Sunday).
            current_time (time): The current time to check for restrictions.
            digit (int): The last digit of the vehicle's license plate.
        Returns:
            bool: True if the vehicle is restricted from circulation, False otherwise.
        Note:
            A vehicle is restricted if all of the following conditions are met:
            - The day of the week is in the rule's list of restricted days
            - The last digit of the license plate is in the rule's list of restricted digits
            - The current time is within the restricted time frame (between start_time and end_time)
        """

        if day_of_week in self.days_of_week and digit in self.restricted_digits:
            if current_time >= self.start_time and current_time <= self.end_time:
                return True
        return False
