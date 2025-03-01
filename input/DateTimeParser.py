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

    def parse_datetime(self, date_time_str: str) -> datetime:
        try:
            return datetime.strptime(date_time_str, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            raise ValueError(f"Unable to parse '{date_time_str}'. Expected format: 'YYYY-MM-DD HH:MM:SS'")