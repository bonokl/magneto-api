from abc import ABC, abstractmethod


class SimulationConfigInterface(ABC):
    @abstractmethod
    def start_simulation(self, sim_req: SimulationStartRequest) -> dict:
        pass
