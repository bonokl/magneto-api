from abc import ABC, abstractmethod
from typing import Optional

from src.entities.design import CreateDesign, Design


class DesignInterface(ABC):
    @abstractmethod
    def get_all(self) -> list[Design]:
        pass

    @abstractmethod
    def get(self, design_id: int) -> Optional[Design]:
        pass

    @abstractmethod
    def create(self, design: CreateDesign) -> Design:
        pass

    @abstractmethod
    def update(self, design_id: int, design: CreateDesign) -> Design:
        pass

    @abstractmethod
    def delete(self, design_id: int) -> None:
        pass
