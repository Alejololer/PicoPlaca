class OutputFormatter:
    """
    A utility class for formatting prediction outputs.
    This class provides a static method to format the boolean result of a license plate restriction prediction
    into a human-readable string message.
    Methods:
        format_prediction(is_restricted: bool) -> str: Formats the restriction prediction as a descriptive message.
    """
    def format_prediction(self, is_restricted: bool) -> str:
        if is_restricted:
            return "Vehicle is restricted to circulate at this time and date"
        else:
            return "Vehicle is not restricted to circulate at this time and date"