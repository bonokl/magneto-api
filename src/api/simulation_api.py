from fastapi import APIRouter

from src.entities.simulation_config import SimulationStartRequest
from src.magneto import container
from src.magneto.repositories.simulation_config_repository import SimulationConfigRepository
from src.magneto.services.simulation_config_service import SimulationConfigService

router = APIRouter()
simulation_service = SimulationConfigService(SimulationConfigRepository())


def start_simulation(sim_req: SimulationStartRequest):
    return container.simulation.start_simulation(sim_req)
