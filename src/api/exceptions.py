# GrowHub | https://github.com/Filip-Vallo/GrowHub/ | /src/api/ | Python 3.9.19

"""
GrowHub API module: exceptions

This module defines custom exception classes used throughout the GrowHub codebase.
These exceptions provide specific error handling for various scenarios related to
command processing, sensor operations, and other potential issues in the system.
Each exception class is designed to capture specific error contexts, allowing
for more granular error handling and debugging in the GrowHub codebase.

Classes:
    CommandError: Base class for command-related exceptions.
    ├── CommandArgumentError: Exception for invalid command argument.
    └── CommandDoesNotExistError: Exception for invalid command (class/method/function does not exist).

    SensorError: Base class for sensor-related exceptions.
    ├── SensorCalibrationError: Exception for sensor calibration issues.
    ├── SensorConfigurationError: Exception for sensor configuration issues.
    ├── SensorConnectionError: Exception for sensor connection issues.
    └── SensorReadError: Exception for sensor read issues.

Usage:
    from exceptions import SensorConnectionError
    from sensors import SensorAquatic

    try:
        # Some operation that might raise an exception
        SensorAquatic.connect()
    except SensorConnectionError as e:
        print(f"Failed to connect to sensor: {e.message}")
"""


# Third-party imports (venv)
from typing import (
    Any,
    Optional
)


class CommandError(Exception):
    """Base class for command-related exceptions."""

    def __init__(self, message: str, parameter: Optional[str] = None) -> None:
        self.message: str = message
        self.parameter: Optional[str] = parameter
        super().__init__(self.message)


class CommandArgumentError(CommandError):
    """Exception for invalid command argument."""

    def __init__(self, message: str, parameter: Optional[str] = None, value: Any = None) -> None:
        super().__init__(message, parameter)
        self.value: Any = value


class CommandDoesNotExistError(CommandError):
    """Exception for invalid command (class/method/function does not exist)."""

    def __init__(self, message: str, command_name: str) -> None:
        super().__init__(message, parameter=command_name)
        self.command_name: str = command_name


class SensorError(Exception):
    """Base class for sensor-related exceptions."""

    def __init__(self, message: str, sensor_type: Optional[str] = None) -> None:
        self.message: str = message
        self.sensor_type: Optional[str] = sensor_type
        super().__init__(self.message)


class SensorCalibrationError(SensorError):
    """Exception for sensor calibration issues."""

    def __init__(self, message: str, sensor_type: Optional[str] = None, calibration_point: Optional[str] = None) \
            -> None:
        super().__init__(message, sensor_type)
        self.calibration_point: Optional[str] = calibration_point


class SensorConfigurationError(SensorError):
    """Exception for sensor configuration issues."""

    def __init__(self, message: str, sensor_type: Optional[str] = None, config_param: Optional[str] = None) -> None:
        super().__init__(message, sensor_type)
        self.config_param: Optional[str] = config_param


class SensorConnectionError(SensorError):
    """Exception for sensor connection issues."""

    def __init__(self, message: str, sensor_type: Optional[str] = None, connection_details: Any = None) -> None:
        super().__init__(message, sensor_type)
        self.connection_details: Any = connection_details


class SensorReadError(SensorError):
    """Exception for sensor reading issues."""

    def __init__(self, message: str, sensor_type: Optional[str] = None, data_type: Optional[str] = None) -> None:
        super().__init__(message, sensor_type)
        self.data_type: Optional[str] = data_type
