from src.magneto.interfaces.simulation_config_interface import SimulationConfigInterface
from src.magneto.repositories.simulation_config_repository import SimulationConfigRepository
from src.entities.simulation_config import SimulationConfig, CreateSimulationConfig, UpdateSimulationConfig
from typing import List, Optional, Tuple

class SimulationConfigService(SimulationConfigInterface):
    def __init__(self, simulation_config_repository: SimulationConfigRepository):
        self._simulation_config_repository = simulation_config_repository

    def get_all_simulation_configs(self, offset: int = 0, limit: int = 100, order_by: Optional[str] = None) -> Tuple[int, List[SimulationConfig]]:
        return self._simulation_config_repository.get_all(offset, limit, order_by)

    def create_simulation_config(self, config: CreateSimulationConfig) -> SimulationConfig:
        return self._simulation_config_repository.create(config)

    def update_simulation_config(self, config_id: int, config: UpdateSimulationConfig) -> SimulationConfig | None:
        return self._simulation_config_repository.update(config_id, config)

    def get_simulation_config(self, config_id: int) -> SimulationConfig | None:
        return self._simulation_config_repository.get(config_id)

    def delete_simulation_config(self, config_id: int) -> bool:
        return self._simulation_config_repository.delete(config_id)
