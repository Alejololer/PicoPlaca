"""
Output Formatter Module

Provides utilities for formatting prediction results into human-readable messages.
"""

class OutputFormatter:
    """
    A utility class for formatting prediction outputs.
    This class provides a static method to format the boolean result of a license plate 
    restriction prediction
    into a human-readable string message.
    Methods:
        format_prediction(is_restricted: bool) -> str: Formats the restriction prediction 
        as a descriptive message.
    """

    @staticmethod
    def format_prediction(is_restricted: bool) -> str:
        """
        Format the prediction result into a human-readable message.
        This function takes the prediction result and returns a message indicating
        whether the vehicle is restricted to circulate or not.
        Args:
            is_restricted (bool): Whether the vehicle is restricted to circulate.
        Returns:
            str: A message indicating whether the vehicle is restricted to circulate.
        """

        if is_restricted:
            return "Vehicle is restricted to circulate at this time and date"
        else:
            return "Vehicle is not restricted to circulate at this time and date"
