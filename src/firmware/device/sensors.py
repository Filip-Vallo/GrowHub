# GrowHub | https://github.com/Filip-Vallo/GrowHub/ | Python 3.9.19

"""
GrowHub firmware module: sensors

This Python module provides classes used to manage interfacing with various connected sensors
used in the GrowHub device.

Supported sensors:
    Pimoroni BME680 Breakout: atmospheric sensor (temperature, humidity, pressure).
    Adafruit STEMMA Soil Sensor: soil sensor (moisture, temperature)

Classes:
    SensorAtmospheric: Manages interfacing with the atmospheric sensor: Pimoroni BME680 Breakout.
    SensorSoil: Manages interfacing with the soil sensor: Adafruit STEMMA Soil Sensor.
    --
    SensorError: Base exception class for sensor-related errors.
    SensorConnectionError: Exception for sensor connection errors.
    SensorConfigurationError: Exception for sensor configuration errors.
    SensorReadError: Exception for sensor reading errors.

Usage:
    from sensors import SensorAtmospheric

    sensor_atmospheric = SensorAtmospheric()
    sensor_atmospheric.connect()
    sensor_atmospheric.setup()
    atmospheric_temperature = sensor_atmospheric.read_temperature()
"""


# Imports: Third-party libraries (venv)
import bme680
import board
from typing import Union, Literal
from adafruit_seesaw.seesaw import Seesaw


# Main classes
class SensorAtmospheric:
    """
    A class to manage interfacing with the atmospheric sensor: Pimoroni BME680 Breakout.

    This class provides methods to connect to the sensor, configure its settings,
    and read temperature, humidity, and pressure data.
    """

    def __init__(self):
        self.sensor: Union[bme680.BME680, None] = None

    def connect(self) -> None:
        """Establish I2C connection with the atmospheric sensor."""
        try:
            self.sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
        except (OSError, IOError) as e:
            raise SensorConnectionError(f"Failed to connect to atmospheric sensor:\n{str(e)}")

    def setup(self) -> None:
        """Configure atmospheric sensor settings."""
        if not self.sensor:
            raise SensorConnectionError("Atmospheric sensor not connected. Cannot execute configuration."
                                        "\nReconnect and try again.")
        else:
            try:
                # Oversampling settings
                self.sensor.set_temperature_oversample(bme680.OS_8X)
                self.sensor.set_humidity_oversample(bme680.OS_2X)
                self.sensor.set_pressure_oversample(bme680.OS_4X)
                # Filter settings
                self.sensor.set_filter(bme680.FILTER_SIZE_3)
            except AttributeError as e:
                raise SensorConfigurationError(f"Atmospheric sensor configuration failed:\n{str(e)}."
                                               f"\nReconnect and try again.")

    def read_temperature(self) -> float:
        """Read atmospheric temperature from the sensor."""
        return self._read_sensor_data('temperature')

    def read_humidity(self) -> float:
        """Read atmospheric humidity from the sensor."""
        return self._read_sensor_data('humidity')

    def read_pressure(self) -> float:
        """Read atmospheric pressure from the sensor."""
        return self._read_sensor_data('pressure')

    # Protected methods
    def _read_sensor_data(self, data_type: Literal['temperature', 'humidity', 'pressure']) -> float:
        """Helper method to read atmospheric sensor data."""
        if not self.sensor:
            raise SensorConnectionError("Atmospheric sensor not connected. Cannot execute data reading."
                                        "\nReconnect and try again.")
        else:
            try:
                value = getattr(self.sensor.data, data_type)
                return round(float(format(value)), 1)
            except AttributeError as e:
                raise SensorReadError(f"Failed to read {data_type} data from the atmospheric sensor:\n{str(e)}"
                                      f"\nReconnect and try again.")


class SensorSoil:
    """
    A class to manage interfacing with the soil sensor: Adafruit STEMMA Soil Sensor.

    This class provides methods to connect to the sensor, configure its settings,
    and read humidity and temperature data.
    """

    def __init__(self):
        self.sensor: Union[Seesaw, None] = None

    def connect(self) -> None:
        """Establish I2C connection with the soil sensor."""
        try:
            self.sensor = Seesaw(board.I2C(), addr=0x36)
        except (OSError, IOError) as e:
            raise SensorConnectionError(f"Failed to connect to soil sensor:\n{str(e)}")

    def setup(self) -> None:
        """Configure soil sensor settings."""
        # No setup required for this sensor
        pass

    def read_moisture(self) -> float:
        """Read soil moisture from the sensor."""
        return self._read_sensor_data('moisture')

    def read_temperature(self) -> float:
        """Read soil temperature from the sensor."""
        return self._read_sensor_data('temperature')

    def _read_sensor_data(self, data_type: Literal['moisture', 'temperature']) -> float:
        """Helper method to read soil sensor data."""
        if not self.sensor:
            raise SensorConnectionError("Soil sensor not connected. Cannot execute data reading."
                                        "\nReconnect and try again.")
        else:
            try:
                if data_type == 'moisture':
                    return self.sensor.moisture_read()
                elif data_type == 'temperature':
                    return self.sensor.get_temp()
            except AttributeError as e:
                raise SensorReadError(f"Failed to read {data_type} data from the soil sensor:\n{str(e)}"
                                      f"\nReconnect and try again.")


# Exception classes
class SensorError(Exception):
    """Base class for sensor-related exceptions."""
    pass


class SensorConnectionError(SensorError):
    """Exception for sensor connection issues."""
    pass


class SensorConfigurationError(SensorError):
    """Exception raised when there's an error in configuring the sensor."""
    pass


class SensorReadError(SensorError):
    """Exception raised when there's an error reading data from the sensor."""
    pass
