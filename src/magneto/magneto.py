from src.magneto import container
from src.magneto.repositories.function_repository import FunctionRepository
from src.magneto.repositories.magnet_material_repository import MagnetMaterialRepository
from src.magneto.repositories.magnet_repository import MagnetRepository
from src.magneto.services.function_service import FunctionService
from src.magneto.services.magnet_materials_service import MagnetMaterialsService
from src.magneto.services.magnet_service import MagnetService


class Magneto:
    @classmethod
    def initialize(cls):
        # sensor_repository = SensorRepository()
        # container.sensors = SensorService(sensor_repository)

        function_repository = FunctionRepository()
        container.functions = FunctionService(function_repository)

        magnet_repository = MagnetRepository()
        container.magnets = MagnetService(magnet_repository)

        magnet_materials_repository = MagnetMaterialRepository()
        container.magnet_materials = MagnetMaterialsService(magnet_materials_repository)

        # design_repository = DesignRepository()
        # container.designs = DesignService(design_repository)
        #
        # simulation_config_repository = SimulationConfigRepository()
        # container.simulation_configs = SimulationConfigService(simulation_config_repository)
