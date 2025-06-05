from abc import ABC, abstractmethod
from typing import List, Optional
from src.entities.design import Design, CreateDesign, UpdateDesign

class DesignInterface(ABC):
    @abstractmethod
    def get_all_designs(self, offset: int = 0, limit: int = 100, order_by: Optional[str] = None) -> (int, List[Design]):
        pass

    @abstractmethod
    def create_design(self, design: CreateDesign) -> Design:
        pass

    @abstractmethod
    def update_design(self, design_id: int, design: UpdateDesign) -> Design | None:
        pass

    @abstractmethod
    def get_design(self, design_id: int) -> Design | None:
        pass

    @abstractmethod
    def delete_design(self, design_id: int) -> bool:
        pass

