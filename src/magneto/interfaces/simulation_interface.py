from abc import ABC, abstractmethod


class SimulationInterface(ABC):
    @abstractmethod
    def simulate(self, design_id: int) -> dict:
        pass
