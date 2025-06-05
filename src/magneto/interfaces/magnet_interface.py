from abc import ABC, abstractmethod
from typing import List, Optional
from src.entities.magnet import Magnet, CreateMagnet, UpdateMagnet

class MagnetInterface(ABC):
    @abstractmethod
    def get_all_magnets(self, offset: int = 0, limit: int = 100, order_by: Optional[str] = None) -> (int, List[Magnet]):
        pass

    @abstractmethod
    def create_magnet(self, magnet: CreateMagnet) -> Magnet:
        pass

    @abstractmethod
    def update_magnet(self, magnet_id: int, magnet: UpdateMagnet) -> Magnet | None:
        pass

    @abstractmethod
    def get_magnet(self, magnet_id: int) -> Magnet | None:
        pass

    @abstractmethod
    def delete_magnet(self, magnet_id: int) -> bool:
        pass

