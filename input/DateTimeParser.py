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
        date_time_str: str = date_str + " " + time_str
        try:
            return datetime.strptime(date_time_str, "%Y-%m-%d %H:%M")
        except ValueError:
            raise ValueError(f"Unable to parse '{date_time_str}'. Expected format: 'YYYY-MM-DD HH:MM:SS'")