# GrowHub | https://github.com/Filip-Vallo/GrowHub/ | /src/firmware/ | Python 3.9.19

"""
GrowHub firmware module: sensors

This module provides classes to manage interfacing with various connected sensors
used in the GrowHub device.

Supported sensors:
    Atlas Scientific EZO Conductivity Sensor: aquatic sensor (EC).
    Atlas Scientific EZO pH Sensor: aquatic sensor (pH).
    Pimoroni BME680 Breakout: atmospheric sensor (temperature, humidity, pressure).
    Adafruit STEMMA Soil Sensor: soil sensor (moisture, temperature).

Classes:
    SensorAquatic: Manages interfacing with the aquatic sensors: Atlas Scientific EZO pH and Conductivity sensors.
    SensorAtmospheric: Manages interfacing with the atmospheric sensor: Pimoroni BME680 Breakout.
    SensorSoil: Manages interfacing with the soil sensor: Adafruit STEMMA Soil Sensor.

Usage:
    from sensors import SensorAtmospheric

    sensor_atmospheric = SensorAtmospheric()
    sensor_atmospheric.connect()
    sensor_atmospheric.setup()
    atmospheric_temperature = sensor_atmospheric.read_temperature()
"""


# Third-party imports (venv)
import bme680
import board
from atlas_i2c import AtlasI2C
from atlas_i2c.commands import (
    CalibratePh,
    Read,
    Status
)
from adafruit_seesaw.seesaw import Seesaw
from typing import (
    Literal,
    Union
)
# Codebase imports (API)
from api_client import APIClient
CommandArgumentError = APIClient.get_exception('CommandArgumentError')
SensorCalibrationError = APIClient.get_exception('SensorCalibrationError')
SensorConfigurationError = APIClient.get_exception('SensorConfigurationError')
SensorConnectionError = APIClient.get_exception('SensorConnectionError')
SensorReadError = APIClient.get_exception('SensorReadError')


class SensorAquatic:
    """
    Manages interfacing with the aquatic sensors: Atlas Scientific EZO pH and Conductivity (EC) sensors.

    This class provides methods to connect to the sensors via I2C interface, configure their settings,
    calibrate pH probe, and read pH and conductivity data.
    """

    PH_I2C_ADDRESS = 0x63
    EC_I2C_ADDRESS = 0x64
    decimal_precision = {'ph': 1, 'ec': 0}

    def __init__(self):
        self.ph_sensor: Union[AtlasI2C, None] = None
        self.ec_sensor: Union[AtlasI2C, None] = None

    def connect(self) -> None:
        """Establishes I2C connection with the aquatic sensors."""
        try:
            self.ph_sensor = AtlasI2C(address=self.PH_I2C_ADDRESS)
            self.ec_sensor = AtlasI2C(address=self.EC_I2C_ADDRESS)
        except (OSError, IOError) as e:
            raise SensorConnectionError(f"Failed to connect to aquatic sensors:\n{str(e)}", sensor_type="Aquatic")

    def setup(self) -> None:
        """Configures aquatic sensor settings."""
        # No configuration required for this sensor
        pass

    def calibrate_ph(self, point: Literal['low', 'mid', 'high']) -> None:
        """Calibrates the pH sensor."""
        if not self.ph_sensor:
            raise SensorConnectionError("pH sensor not connected. Cannot execute calibration."
                                        "\nReconnect and try again.", sensor_type="Aquatic")
        else:
            try:
                response = self.ph_sensor.query(CalibratePh.format_command(point))
                if response.status_code != 1:
                    raise SensorCalibrationError(f"pH calibration failed: {response.data.decode()}",
                                                 sensor_type="Aquatic", calibration_point=point)
            except AttributeError as e:
                SensorCalibrationError(f"pH calibration failed:\n{str(e)}", sensor_type="Aquatic",
                                       calibration_point=point)

    def read_ph(self) -> float:
        """Reads pH value from the sensor."""
        return self._read_sensor_data('ph')

    def read_ec(self) -> float:
        """Reads conductivity value from the sensor."""
        return self._read_sensor_data('ec')

    # Protected methods
    def _read_sensor_data(self, data_type: Literal['ph', 'ec']) -> float:
        """Helper method to read aquatic sensor data."""
        sensor = self.ph_sensor if data_type == 'ph' else self.ec_sensor if data_type == 'ec' else None
        if not sensor:
            raise SensorConnectionError(f"{data_type.capitalize()} sensor not connected. Cannot execute data reading."
                                        f"\nReconnect and try again.", sensor_type="Aquatic")
        else:
            try:
                response = sensor.query(Read.format_command())
                if response.status_code != 1:
                    raise SensorReadError(f"Failed to read {data_type} data from the aquatic sensor:"
                                          f"\n{response.data.decode()}\nReconnect and try again.",
                                          parameter="data_type", value=data_type)
                return round(float(response.data.decode()), self.decimal_precision[data_type])
            except (AttributeError, ValueError) as e:
                raise SensorReadError(f"Failed to read {data_type} data from the aquatic sensor:\n{str(e)}"
                                      f"\nReconnect and try again.", sensor_type="Aquatic", data_type=data_type)


class SensorAtmospheric:
    """
    Manages interfacing with the atmospheric sensor: Pimoroni BME680 Breakout.

    This class provides methods to connect to the sensor via I2C interface, configure its settings,
    and read temperature, humidity, and pressure data.
    """

    I2C_ADDRESS = 0x76
    decimal_precision = {'temperature': 1, 'humidity': 0, 'pressure': 0}

    def __init__(self):
        self.sensor: Union[bme680.BME680, None] = None

    def connect(self) -> None:
        """Establishes I2C connection with the atmospheric sensor."""
        try:
            self.sensor = bme680.BME680(self.I2C_ADDRESS)
        except (OSError, IOError) as e:
            raise SensorConnectionError(f"Failed to connect to atmospheric sensor:\n{str(e)}",
                                        sensor_type="Atmospheric")

    def setup(self) -> None:
        """Configures atmospheric sensor settings."""
        if not self.sensor:
            raise SensorConnectionError("Atmospheric sensor not connected. Cannot execute configuration."
                                        "\nReconnect and try again.", sensor_type="Atmospheric")
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
                                               f"\nReconnect and try again.", sensor_type="Atmospheric")

    def read_temperature(self) -> float:
        """Reads atmospheric temperature from the sensor."""
        return self._read_sensor_data('temperature')

    def read_humidity(self) -> float:
        """Reads atmospheric humidity from the sensor."""
        return self._read_sensor_data('humidity')

    def read_pressure(self) -> float:
        """Read atmospheric pressure from the sensor."""
        return self._read_sensor_data('pressure')

    # Protected methods
    def _read_sensor_data(self, data_type: Literal['temperature', 'humidity', 'pressure']) -> float:
        """Helper method to read atmospheric sensor data."""
        if not self.sensor:
            raise SensorConnectionError("Soil sensor not connected. Cannot execute data reading."
                                        "\nReconnect and try again.", sensor_type="Atmospheric")
        else:
            try:
                if data_type not in ['temperature', 'humidity', 'pressure']:
                    raise CommandArgumentError(f"Cannot read {data_type} from the soil sensor. Invalid data type. "
                                               f"\nChoose either moisture or temperature.", parameter="data_type",
                                               value=data_type)
                else:
                    value = getattr(self.sensor.data, data_type)
                    return round(float(value), self.decimal_precision[data_type])
            except (AttributeError, ValueError) as e:
                raise SensorReadError(f"Failed to read {data_type} data from the soil sensor:\n{str(e)}"
                                      f"\nReconnect and try again.", sensor_type="Atmospheric", data_type=data_type)


class SensorSoil:
    """
    Manages interfacing with the soil sensor: Adafruit STEMMA Soil Sensor.

    This class provides methods to connect to the sensor via I2C interface, configure its settings,
    and read humidity and temperature data.
    """

    I2C_ADDRESS = 0x36
    decimal_precision = {'moisture': 0, 'temperature': 0}

    def __init__(self):
        self.sensor: Union[Seesaw, None] = None

    def connect(self) -> None:
        """Establishes I2C connection with the soil sensor."""
        try:
            self.sensor = Seesaw(board.I2C(), addr=self.I2C_ADDRESS)
        except (OSError, IOError) as e:
            raise SensorConnectionError(f"Failed to connect to soil sensor:\n{str(e)}", sensor_type="Soil")

    def setup(self) -> None:
        """Configures soil sensor settings."""
        # No configuration required for this sensor
        pass

    def read_moisture(self) -> float:
        """Reads soil moisture from the sensor."""
        return self._read_sensor_data('moisture')

    def read_temperature(self) -> float:
        """Reads soil temperature from the sensor."""
        return self._read_sensor_data('temperature')

    # Protected methods
    def _read_sensor_data(self, data_type: Literal['moisture', 'temperature']) -> float:
        """Helper method to read soil sensor data."""
        if not self.sensor:
            raise SensorConnectionError("Soil sensor not connected. Cannot execute data reading."
                                        "\nReconnect and try again.", sensor_type="Soil")
        else:
            try:
                if data_type == 'moisture':
                    value = self.sensor.moisture_read()
                    return round(float(value), self.decimal_precision[data_type])
                elif data_type == 'temperature':
                    value = self.sensor.get_temp()
                    return round(float(value), self.decimal_precision[data_type])
                else:
                    raise CommandArgumentError(f"Cannot read {data_type} from the soil sensor. Invalid data type."
                                               f"\nChoose either moisture or temperature.", parameter="data_type",
                                               value=data_type)
            except (AttributeError, ValueError) as e:
                raise SensorReadError(f"Failed to read {data_type} data from the soil sensor:\n{str(e)}"
                                      f"\nReconnect and try again.", sensor_type="Soil", data_type=data_type)
