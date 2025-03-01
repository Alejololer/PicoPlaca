"""
The input module contains utilities for parsing and validating user input data.
"""
from .date_time_parser import DateTimeParser
from .license_plate_parser import LicensePlateParser

__all__ = ["DateTimeParser", "LicensePlateParser"]
