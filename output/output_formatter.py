"""
Output Formatter Module

This module provides utilities for formatting the prediction outputs of the Pico y Placa system.
It contains the OutputFormatter class which converts boolean restriction results into
human-readable messages for end users.

The module is part of the PicoPlaca project which helps users determine if a vehicle
is restricted from circulation based on license plate, date, and time according to
local traffic restriction regulations.
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
