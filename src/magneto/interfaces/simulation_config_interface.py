from abc import ABC, abstractmethod

from src.entities.simulation_config import SimulationStartRequest


class SimulationConfigInterface(ABC):
    @abstractmethod
    def start_simulation(self, sim_req: SimulationStartRequest) -> dict:
        pass
