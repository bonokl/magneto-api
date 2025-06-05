from src.magneto.interfaces.magnet_interface import MagnetInterface
from src.magneto.repositories.magnet_repository import MagnetRepository
from src.entities.magnet import Magnet, CreateMagnet, UpdateMagnet
from typing import List, Optional, Tuple

class MagnetService(MagnetInterface):
    def __init__(self, magnet_repository: MagnetRepository):
        self._magnet_repository = magnet_repository

    def get_all_magnets(self, offset: int = 0, limit: int = 100, order_by: Optional[str] = None) -> Tuple[int, List[Magnet]]:
        return self._magnet_repository.get_all(offset, limit, order_by)

    def create_magnet(self, magnet: CreateMagnet) -> Magnet:
        return self._magnet_repository.create(magnet)

    def update_magnet(self, magnet_id: int, magnet: UpdateMagnet) -> Magnet | None:
        return self._magnet_repository.update(magnet_id, magnet)

    def get_magnet(self, magnet_id: int) -> Magnet | None:
        return self._magnet_repository.get(magnet_id)

    def delete_magnet(self, magnet_id: int) -> bool:
        return self._magnet_repository.delete(magnet_id)
