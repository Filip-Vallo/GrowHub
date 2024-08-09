# GrowHub | https://github.com/Filip-Vallo/GrowHub/ | /src/api/ | Python 3.9.19

"""
GrowHub API endpoint: exceptions_api

This module provides an API endpoint for retrieving exception classes
defined in the main exceptions module. It acts as a bridge between the API
and the core exception handling system of GrowHub. This module is designed
to be used within the API context, allowing dynamic access to exception classes.

The module imports all exception classes from the main exceptions module
and provides a function to retrieve these exceptions by name.

Functions:
    get_exception: Returns the exception class corresponding to the given exception name.

Usage:
    from exceptions_api import get_exception

    # Retrieve a specific exception class
    SensorError = get_exception('SensorError')

    # Use the retrieved exception
    try:
        # Some operation
        raise SensorError("An error occurred", sensor_type="TemperatureSensor")
    except SensorError as e:
        print(f"Sensor error: {e.message}, Type: {e.sensor_type}")
"""


# Third-party imports (venv)
from typing import Type
# Codebase imports
from exceptions import (
    CommandError,
    CommandArgumentError,
    CommandDoesNotExistError,
    SensorError,
    SensorCalibrationError,
    SensorConfigurationError,
    SensorConnectionError,
    SensorReadError
)


__all__ = ['get_exception']


class ExceptionDoesNotExistError(Exception):
    """Raises exception when invalid exception name is provided."""
    pass


def get_exception(exception_name: str) -> Type[Exception]:
    """
    Retrieves an exception class by its name.

    Args:
        exception_name (str): The name of the exception class to retrieve.

    Usage:
        SensorError = get_exception('SensorError')
    """

    exceptions = {
        'CommandError': CommandError,
        'CommandArgumentError': CommandArgumentError,
        'CommandDoesNotExistError': CommandDoesNotExistError,
        'SensorError': SensorError,
        'SensorCalibrationError': SensorCalibrationError,
        'SensorConfigurationError': SensorConfigurationError,
        'SensorConnectionError': SensorConnectionError,
        'SensorReadError': SensorReadError
    }

    exception_class = exceptions.get(exception_name)
    if exception_class is None:
        raise ExceptionDoesNotExistError(f"Unknown exception name: {exception_name}")

    return exception_class
