from datetime import datetime


class DateTimeParser:
    """
    A class for parsing datetime strings into datetime objects.
    This class provides a method to convert a string representation of date and time
    into a Python datetime object using a specific format.
    Attributes:
        None
    Methods:
        parse_datetime(date_time_str: str) -> datetime:
            Parse a string representation of date and time into a datetime object.
    """

    def parse_datetime(self, date_time_str: str) -> datetime:
        return datetime.strptime(date_time_str, "%Y-%m-%d %H:%M:%S")