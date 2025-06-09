import magpylib as magpy
from scipy.constants import mu_0
from scipy.spatial.transform import Rotation as R

from src.entities.design import Design
from src.entities.magnet import MagnetShape
from src.magneto.interfaces.simulation_interface import SimulationInterface
from src.magneto.repositories.design_repository import DesignRepository
from src.magneto.repositories.magnet_repository import MagnetRepository


class SimulationService(SimulationInterface):

    def __init__(self, design_repository: DesignRepository, magnet_repository: MagnetRepository):
        self._design_repository = design_repository
        self._magnet_repository = magnet_repository

    def simulate(self, design_id: int) -> dict:
        design = self._design_repository.get(design_id)
        magnet = self._create_magnet(design)
        sensor = self._create_sensor(design)

        points = [sensor.position]  # in SI Units (m)
        B = magpy.getB(magnet, points)

        return B

    def _create_magnet(self, design: Design):
        magnet = self._magnet_repository.get(design.magnet_id)

        if magnet is None:
            return None

        if magnet.shape == MagnetShape.BAR:
            position = (design.magnet_position.x_position / 1000, design.magnet_position.y_position / 1000,
                        design.magnet_position.z_position / 1000)
            dimension = (design.magnet_geometry.magnet_length_x / 1000, design.magnet_geometry.magnet_length_y / 1000,
                         design.magnet_geometry.magnet_length_z / 1000)
            orientation = R.from_rotvec(
                (design.magnet_angle.x_angle, design.magnet_angle.y_angle, design.magnet_angle.z_angle),
                degrees=True)
            magnetization = self._calculate_magnetization(design)
            m = magpy.magnet.Cuboid(position=position, dimension=dimension, orientation=orientation,
                                    magnetization=magnetization)
            return m

        return None

    def _create_sensor(self, design: Design):
        return magpy.Sensor(position=(0, 0, -0.05))

    def _calculate_magnetization(self, design: Design) -> list[float]:
        """
        Calculate the magnetization vector (A/m) for the given design.
        Magnetization M = Br_effective / mu0, along z-axis by default.
        """

        T_ref = 20  # Reference temperature in Celsius
        # Convert temperature_coefficient from percent to fraction if needed
        temp_coeff = design.temperature_coefficient
        if abs(temp_coeff) > 1:
            temp_coeff = temp_coeff / 100.0
        Br_effective = design.remanence * (1 + temp_coeff * (design.temperature - T_ref))
        M = Br_effective / mu_0
        return [0.0, 0.0, M]
