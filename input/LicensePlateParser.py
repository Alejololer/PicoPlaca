import re


class LicensePlateParser:
    """
    LicensePlateParser class
    A class that provides functionality for validating license plate numbers.
    Methods:
        parseLicensePlate(license_plate: str) -> int:
            Validates if a license plate string matches the expected format and returns the last digit.
            Args:
                license_plate (str): The license plate string to validate in format "XXX-###" or "XXX-####",
                                    where X is an uppercase letter and # is a digit.
            Returns:
                int: The last digit of the license plate as an integer if the format is valid.
            Raises:
                ValueError: If the license plate format is invalid or an error occurs during validation.
    """

    @staticmethod
    def parseLicensePlate(license_plate: str) -> int:
        try:
            # Check if format is valid
            if re.match("^[A-Z]{3}-[0-9]{3,4}$", license_plate):
                # Extract the last character and convert to integer
                return int(license_plate[-1])
            else:
                raise ValueError(f"Invalid license plate format: '{license_plate}'. Expected format: 'XXX-###' or 'XXX-####'")
        except Exception as e:
            raise ValueError(f"Unable to parse '{str(e)}'. Expected format: 'XXX-###' or 'XXX-####'")