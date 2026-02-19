#!/usr/bin/env python3
"""
Field Node sensor integration for Pi Zero 2 W.
Reads BME280, DS18B20, GPS, MLX90614, DS3231 RTC, and BH1750.
Designed for the actual component inventory.
"""

import time
import json
import os
from pathlib import Path
from datetime import datetime

# ── Sensor availability flags ──
HAS_BME280 = False
HAS_GPS = False
HAS_MLX90614 = False
HAS_DS18B20 = False
HAS_BH1750 = False
HAS_DS3231 = False

try:
    import smbus2
    import bme280
    HAS_BME280 = True
except ImportError:
    pass

try:
    import serial
    HAS_GPS = True
except ImportError:
    pass

try:
    from smbus2 import SMBus
    HAS_MLX90614 = True
except ImportError:
    pass

LOG_DIR = Path("/opt/fieldnode/data/sensor_logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)


class BME280Sensor:
    """Barometric pressure, temperature, humidity — critical for weather forecasting."""
    ADDRESS = 0x76

    def __init__(self, bus_num=1):
        self.bus = smbus2.SMBus(bus_num)
        self.calibration = bme280.load_calibration_params(self.bus, self.ADDRESS)

    def read(self):
        data = bme280.sample(self.bus, self.ADDRESS, self.calibration)
        return {
            "temperature_c": round(data.temperature, 1),
            "humidity_pct": round(data.humidity, 1),
            "pressure_hpa": round(data.pressure, 1),
        }


class DS18B20Sensor:
    """Waterproof temperature probe (1-Wire on GPIO 4)."""
    BASE_DIR = "/sys/bus/w1/devices"

    def __init__(self):
        self.devices = []
        if os.path.exists(self.BASE_DIR):
            self.devices = [
                d for d in os.listdir(self.BASE_DIR)
                if d.startswith("28-")
            ]

    def read_all(self):
        temps = {}
        for dev in self.devices:
            path = Path(self.BASE_DIR) / dev / "w1_slave"
            try:
                text = path.read_text()
                if "YES" in text:
                    temp_str = text.split("t=")[1].strip()
                    temps[dev] = round(int(temp_str) / 1000.0, 1)
            except Exception:
                pass
        return temps


class GPSSensor:
    """GY-NEO6MV2 GPS on UART (/dev/serial0)."""

    def __init__(self, port="/dev/serial0", baud=9600):
        self.ser = serial.Serial(port, baud, timeout=2)
        self.last_fix = None

    def read(self):
        """Try to get a GGA fix. Returns dict or None."""
        for _ in range(20):  # read up to 20 lines looking for GGA
            try:
                line = self.ser.readline().decode("ascii", errors="replace").strip()
            except Exception:
                continue
            if "$GPGGA" in line or "$GNGGA" in line:
                return self._parse_gga(line)
        return self.last_fix

    def _parse_gga(self, line):
        parts = line.split(",")
        if len(parts) < 10 or not parts[2]:
            return None
        try:
            lat = self._nmea_to_decimal(parts[2], parts[3])
            lon = self._nmea_to_decimal(parts[4], parts[5])
            fix_quality = int(parts[6])
            sats = int(parts[7])
            alt = float(parts[9]) if parts[9] else 0
            self.last_fix = {
                "lat": round(lat, 6),
                "lon": round(lon, 6),
                "altitude_m": round(alt, 1),
                "satellites": sats,
                "fix_quality": fix_quality,
                "timestamp": parts[1][:6],
            }
            return self.last_fix
        except (ValueError, IndexError):
            return None

    @staticmethod
    def _nmea_to_decimal(coord, direction):
        deg = int(float(coord) / 100)
        minutes = float(coord) - deg * 100
        decimal = deg + minutes / 60
        if direction in ("S", "W"):
            decimal = -decimal
        return decimal


class MLX90614Sensor:
    """Non-contact IR thermometer (I2C)."""
    ADDRESS = 0x5A

    def __init__(self, bus_num=1):
        self.bus = SMBus(bus_num)

    def read(self):
        try:
            obj_raw = self.bus.read_word_data(self.ADDRESS, 0x07)
            amb_raw = self.bus.read_word_data(self.ADDRESS, 0x06)
            return {
                "object_temp_c": round(obj_raw * 0.02 - 273.15, 1),
                "ambient_temp_c": round(amb_raw * 0.02 - 273.15, 1),
            }
        except Exception:
            return None


class BH1750Sensor:
    """Light intensity sensor (I2C)."""
    ADDRESS = 0x23

    def __init__(self, bus_num=1):
        self.bus = SMBus(bus_num)

    def read(self):
        try:
            self.bus.write_byte(self.ADDRESS, 0x10)  # continuous high-res mode
            time.sleep(0.2)
            data = self.bus.read_i2c_block_data(self.ADDRESS, 0x10, 2)
            lux = (data[0] << 8 | data[1]) / 1.2
            return {"lux": round(lux, 1)}
        except Exception:
            return None


class SensorHub:
    """Unified sensor interface for the Field Node."""

    def __init__(self):
        self.sensors = {}
        self._init_sensors()

    def _init_sensors(self):
        if HAS_BME280:
            try:
                self.sensors["bme280"] = BME280Sensor()
            except Exception:
                pass

        try:
            ds = DS18B20Sensor()
            if ds.devices:
                self.sensors["ds18b20"] = ds
        except Exception:
            pass

        if HAS_GPS:
            try:
                self.sensors["gps"] = GPSSensor()
            except Exception:
                pass

        if HAS_MLX90614:
            try:
                self.sensors["mlx90614"] = MLX90614Sensor()
            except Exception:
                pass

        if HAS_BH1750:
            try:
                self.sensors["bh1750"] = BH1750Sensor()
            except Exception:
                pass

    def read_all(self):
        """Read all available sensors. Returns dict."""
        readings = {"timestamp": datetime.now().isoformat(), "sensors": {}}

        if "bme280" in self.sensors:
            try:
                readings["sensors"]["environment"] = self.sensors["bme280"].read()
            except Exception:
                pass

        if "ds18b20" in self.sensors:
            try:
                readings["sensors"]["probes"] = self.sensors["ds18b20"].read_all()
            except Exception:
                pass

        if "gps" in self.sensors:
            try:
                fix = self.sensors["gps"].read()
                if fix:
                    readings["sensors"]["gps"] = fix
            except Exception:
                pass

        if "mlx90614" in self.sensors:
            try:
                ir = self.sensors["mlx90614"].read()
                if ir:
                    readings["sensors"]["ir_temp"] = ir
            except Exception:
                pass

        if "bh1750" in self.sensors:
            try:
                lux = self.sensors["bh1750"].read()
                if lux:
                    readings["sensors"]["light"] = lux
            except Exception:
                pass

        return readings

    def log_reading(self):
        """Take a reading and append to today's log file."""
        reading = self.read_all()
        today = datetime.now().strftime("%Y-%m-%d")
        log_file = LOG_DIR / f"sensors-{today}.jsonl"
        with log_file.open("a") as f:
            f.write(json.dumps(reading) + "\n")
        return reading

    def available(self):
        """List available sensor names."""
        return list(self.sensors.keys())

    def pressure_trend(self, hours=3):
        """Read recent pressure logs and return trend (rising/falling/stable).
        Critical for weather forecasting."""
        today = datetime.now().strftime("%Y-%m-%d")
        log_file = LOG_DIR / f"sensors-{today}.jsonl"
        if not log_file.exists():
            return "insufficient_data"

        pressures = []
        cutoff = time.time() - (hours * 3600)
        for line in log_file.read_text().strip().split("\n"):
            try:
                entry = json.loads(line)
                ts = datetime.fromisoformat(entry["timestamp"]).timestamp()
                if ts > cutoff and "environment" in entry.get("sensors", {}):
                    pressures.append(entry["sensors"]["environment"]["pressure_hpa"])
            except Exception:
                continue

        if len(pressures) < 2:
            return "insufficient_data"

        delta = pressures[-1] - pressures[0]
        if delta > 2:
            return "rising"  # improving weather likely
        elif delta < -2:
            return "falling"  # deteriorating weather likely
        else:
            return "stable"


if __name__ == "__main__":
    hub = SensorHub()
    print(f"Available sensors: {hub.available()}")
    reading = hub.read_all()
    print(json.dumps(reading, indent=2))
