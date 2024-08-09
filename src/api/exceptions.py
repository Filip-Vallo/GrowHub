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

    def __str__(self) -> str:
        return (f"CommandError: {self.message}"
                + (f" (Parameter: {self.parameter})" if self.parameter else ""))


class CommandArgumentError(CommandError):
    """Raises exception when invalid command argument is provided."""

    def __init__(self, message: str, parameter: Optional[str] = None, value: Any = None) -> None:
        super().__init__(message, parameter)
        self.value: Any = value

    def __str__(self) -> str:
        return (f"CommandArgumentError: {self.message}"
                + (f" (Parameter: {self.parameter})" if self.parameter else "")
                + (f" (Value: {self.value})" if self.value is not None else ""))


class CommandDoesNotExistError(CommandError):
    """Raises exception when invalid command name is provided (class/method/function does not exist)."""

    def __init__(self, message: str, command_name: str) -> None:
        super().__init__(message, parameter=command_name)
        self.command_name: str = command_name

    def __str__(self) -> str:
        return (f"CommandDoesNotExistError: {self.message}"
                + f" (Command: {self.command_name})")


class SensorError(Exception):
    """Base class for sensor-related exceptions."""

    def __init__(self, message: str, sensor_type: Optional[str] = None) -> None:
        self.message: str = message
        self.sensor_type: Optional[str] = sensor_type
        super().__init__(self.message)

    def __str__(self) -> str:
        return (f"SensorError: {self.message}"
                + (f" (Sensor Type: {self.sensor_type})" if self.sensor_type else ""))


class SensorCalibrationError(SensorError):
    """Raises exception when sensor calibration issues are detected."""

    def __init__(self, message: str, sensor_type: Optional[str] = None, calibration_point: Optional[str] = None) \
            -> None:
        super().__init__(message, sensor_type)
        self.calibration_point: Optional[str] = calibration_point

    def __str__(self) -> str:
        return (f"SensorCalibrationError: {self.message}"
                + (f" (Sensor Type: {self.sensor_type})" if self.sensor_type else "")
                + (f" (Calibration Point: {self.calibration_point})" if self.calibration_point else ""))


class SensorConfigurationError(SensorError):
    """Raises exception when sensor configuration issues are detected."""

    def __init__(self, message: str, sensor_type: Optional[str] = None, config_param: Optional[str] = None) -> None:
        super().__init__(message, sensor_type)
        self.config_param: Optional[str] = config_param

    def __str__(self) -> str:
        return (f"SensorConfigurationError: {self.message}"
                + (f" (Sensor Type: {self.sensor_type})" if self.sensor_type else "")
                + (f" (Config Parameter: {self.config_param})" if self.config_param else ""))


class SensorConnectionError(SensorError):
    """Raises exception when sensor connection issues are detected."""

    def __init__(self, message: str, sensor_type: Optional[str] = None, connection_details: Any = None) -> None:
        super().__init__(message, sensor_type)
        self.connection_details: Any = connection_details

    def __str__(self) -> str:
        return (f"SensorConnectionError: {self.message}"
                + (f" (Sensor Type: {self.sensor_type})" if self.sensor_type else "")
                + (f" (Connection Details: {self.connection_details})" if self.connection_details else ""))


class SensorReadError(SensorError):
    """Raises exception when sensor reading issues are detected."""

    def __init__(self, message: str, sensor_type: Optional[str] = None, data_type: Optional[str] = None) -> None:
        super().__init__(message, sensor_type)
        self.data_type: Optional[str] = data_type

    def __str__(self) -> str:
        return (f"SensorReadError: {self.message}"
                + (f" (Sensor Type: {self.sensor_type})" if self.sensor_type else "")
                + (f" (Data Type: {self.data_type})" if self.data_type else ""))
