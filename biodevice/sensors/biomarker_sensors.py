from dataclasses import dataclass
from datetime import datetime
import random

@dataclass
class SensorReading:
    sensor_id: str
    value: float
    unit: str
    timestamp: str

class BiomarkerSensor:
    def __init__(self, sensor_id: str, unit: str):
        self.sensor_id = sensor_id
        self.unit = unit

    def read(self) -> SensorReading:
        raise NotImplementedError

class SimulatedSensor(BiomarkerSensor):
    def read(self) -> SensorReading:
        return SensorReading(
            sensor_id=self.sensor_id,
            value=round(random.uniform(0, 100), 2),
            unit=self.unit,
            timestamp=datetime.now().isoformat(),
        )

def initialize_sensors():
    return [
        SimulatedSensor("biomarker_1", "unit"),
        SimulatedSensor("biomarker_2", "unit"),
        SimulatedSensor("biomarker_3", "unit"),
        SimulatedSensor("biomarker_4", "unit"),
    ]

def read_all_sensors(sensors):
    return [sensor.read() for sensor in sensors]
