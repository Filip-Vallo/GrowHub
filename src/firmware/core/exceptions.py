# GrowHub | https://github.com/Filip-Vallo/GrowHub/ | Python 3.9.19

# Third-party libraries (venv)
from typing import (
    Any,
    Optional
)


class CommandError(Exception):
    """Base class for command-related exceptions (invalid values in module's parameter)."""

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
