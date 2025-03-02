"""
Date Time Parser Module

Converts string representations of dates and times into datetime objects for restriction rules.
"""
from datetime import datetime


class DateTimeParser:
    """
    Parses datetime strings into datetime objects.
    
    Methods:
        parse_datetime(date_time_str: str) -> datetime:
            Parses a date and time string in 'YYYY-MM-DD HH:MM:SS' format.
        Returns:
            datetime: The parsed datetime object.
        Raises:
            ValueError: If the string format is invalid or cannot be parsed.
    """

    @staticmethod
    def parse_datetime(date_str: str, time_str: str) -> datetime:
        """
        Combines and parses date and time strings into a datetime object.
        Args:
            date_str (str): The date string in format 'YYYY-MM-DD'.
            time_str (str): The time string in format 'HH:MM'.
        Returns:
            datetime: A datetime object representing the parsed date and time.
        Raises:
            ValueError: If the combined date and time string cannot be parsed 
                      with the expected format 'YYYY-MM-DD HH:MM'.
        """

        date_time_str: str = date_str + " " + time_str
        try:
            return datetime.strptime(date_time_str, "%Y-%m-%d %H:%M")
        except ValueError as exc:
            error_msg = "Unable to parse '{}'. Expected format: 'YYYY-MM-DD HH:MM'"
            raise ValueError(error_msg.format(date_time_str)) from exc
