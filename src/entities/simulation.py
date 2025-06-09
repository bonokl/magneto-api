from pydantic import BaseModel


class SimulationResult(BaseModel):
    b_x: list[float]
    b_y: list[float]
    b_z: list[float]
    magnitude: float
