from abc import ABC, abstractmethod
from typing import List
from src.entities.magnet import Magnet

class MagnetInterface(ABC):
    @abstractmethod
    def get_all_magnets(self) -> List[Magnet]:
        pass

    @abstractmethod
    def get_magnet(self, magnet_id: int) -> Magnet | None:
        pass

