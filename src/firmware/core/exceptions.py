# GrowHub | https://github.com/Filip-Vallo/GrowHub/ | Python 3.9.19

# Third-party libraries (venv)
from typing import Any, Optional


class ParameterError(Exception):
    """Base class for value-related exceptions (invalid values in module's parameter)."""

    def __init__(self, message: str, parameter: Optional[str] = None) -> None:
        self.message: str = message
        self.parameter: Optional[str] = parameter
        super().__init__(self.message)


class SensorError(Exception):
    """Base class for sensor-related exceptions."""

    def __init__(self, message: str, sensor_type: Optional[str] = None) -> None:
        self.message: str = message
        self.sensor_type: Optional[str] = sensor_type
        super().__init__(self.message)


class SensorConnectionError(SensorError):
    """Exception for sensor connection issues."""

    def __init__(self, message: str, sensor_type: Optional[str] = None, connection_details: Any = None) -> None:
        super().__init__(message, sensor_type)
        self.connection_details: Any = connection_details


class SensorConfigurationError(SensorError):
    """Exception raised when there's an error in configuring the sensor."""

    def __init__(self, message: str, sensor_type: Optional[str] = None, config_param: Optional[str] = None) -> None:
        super().__init__(message, sensor_type)
        self.config_param: Optional[str] = config_param


class SensorReadError(SensorError):
    """Exception raised when there's an error reading data from the sensor."""

    def __init__(self, message: str, sensor_type: Optional[str] = None, data_type: Optional[str] = None) -> None:
        super().__init__(message, sensor_type)
        self.data_type: Optional[str] = data_type
