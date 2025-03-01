import re


class LicensePlateParser:
    """
    LicensePlateParser class
    A class that provides functionality for validating license plate numbers.
    Methods:
        parseLicensePlate(license_plate: str) -> int:
            Validates if a license plate string matches the expected format.
            Args:
                license_plate (str): The license plate string to validate in format "XXX-###" or "XXX-####",
                                    where X is an uppercase letter and # is a digit.
            Returns:
                int: True if the license plate matches the expected format, False otherwise.
            Raises:
                ValueError: If an error occurs during the validation process.
    """

    @staticmethod
    def parseLicensePlate(license_plate: str) -> int:
        try:
            return bool(re.match("^[A-Z]{3}-[0-9]{3,4}$", license_plate))
        except Exception as e:
            raise ValueError(f"Unable to parse '{str(e)}'. Expected format: 'XXX-###' or 'XXX-####'")