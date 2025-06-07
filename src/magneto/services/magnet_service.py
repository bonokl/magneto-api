from typing import List

from src.entities.magnet import Magnet
from src.magneto.interfaces.magnet_interface import MagnetInterface
from src.magneto.repositories.magnet_repository import MagnetRepository


class MagnetService(MagnetInterface):
    def __init__(self, magnet_repository: MagnetRepository):
        self._magnet_repository = magnet_repository

    def get_all_magnets(self) -> List[Magnet]:
        return self._magnet_repository.get_all()

    def get_magnet(self, magnet_id: int) -> Magnet | None:
        return self._magnet_repository.get(magnet_id)
