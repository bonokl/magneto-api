from abc import ABC, abstractmethod
from typing import List, Optional
from src.entities.simulation_config import SimulationConfig, CreateSimulationConfig, UpdateSimulationConfig

class SimulationConfigInterface(ABC):
    @abstractmethod
    def get_all_simulation_configs(self, offset: int = 0, limit: int = 100, order_by: Optional[str] = None) -> (int, List[SimulationConfig]):
        pass

    @abstractmethod
    def create_simulation_config(self, config: CreateSimulationConfig) -> SimulationConfig:
        pass

    @abstractmethod
    def update_simulation_config(self, config_id: int, config: UpdateSimulationConfig) -> SimulationConfig | None:
        pass

    @abstractmethod
    def get_simulation_config(self, config_id: int) -> SimulationConfig | None:
        pass

    @abstractmethod
    def delete_simulation_config(self, config_id: int) -> bool:
        pass

