from src.entities.sensor import Sensor
from typing import List

sensors = [
            Sensor(
                id="TMAG3001",
                sensorName="TMAG3001",
                category="Multi-axis linear & angle position sensors",
                variant=["TMAG3001A2YBGR", "TMAG3001A1YBGR"],
                package=["DSBGA"],
                pin_count=["6"],
                specification={
                    "blockDiagramUrl": "https://www.ti.com//ds_dgm/images/fbd_slys053c.svg",
                    "description": "Three-axis linear Hall-effect sensor with I²C and programmable switch in wafer chip-scale package",
                    "ProductPageUrl": "https://www.ti.com/product/TMAG3001"
                }
            ),
            Sensor(
                id="TMAG6180-Q1",
                sensorName="TMAG6180-Q1",
                category="Multi-axis linear & angle position sensors",
                variant=["TMAG6180EDGKRQ1"],
                package=["VSSOP"],
                pin_count=["8"],
                specification={
                    "blockDiagramUrl": "https://www.ti.com//ds_dgm/images/fbd_slys037a.svg",
                    "description": "Automotive high-precision analog AMR angle sensor with 360° angle range",
                    "ProductPageUrl": "https://www.ti.com/product/TMAG6180-Q1"
                }
            ),
            Sensor(
                id="TMAG6181-Q1",
                sensorName="TMAG6181-Q1",
                category="Multi-axis linear & angle position sensors",
                variant=["TMAG6181EDGKRQ1"],
                package=["VSSOP"],
                pin_count=["8"],
                specification={
                    "blockDiagramUrl": "https://www.ti.com//ds_dgm/images/fbd_slys048b_2.svg",
                    "description": "Automotive high-precision analog AMR angle sensor with integrated turns\ncounter",
                    "ProductPageUrl": "https://www.ti.com/product/TMAG6181-Q1"
                }
            ),
        ]

class SensorRepository:
    def get(self, sensor_id: int) -> Sensor | None:
        for s in sensors:
            if s.id == sensor_id:
                return s
        return None

    def get_all(self,) -> List[Sensor]:
        return sensors

