from typing import List, Optional

from src.entities.design import CreateDesign, Design
from src.magneto.interfaces.design_interface import DesignInterface
from src.magneto.repositories.design_repository import DesignRepository


class DesignService(DesignInterface):
    def __init__(self, design_repository: DesignRepository):
        self._design_repository = design_repository

    def get_all(self) -> List[Design]:
        return self._design_repository.get_all()

    def get(self, design_id: int) -> Optional[Design]:
        return self._design_repository.get(design_id)

    def create(self, design: CreateDesign) -> Design:
        return self._design_repository.create(design)

    def update(self, design_id: int, design: CreateDesign) -> Design:
        return self._design_repository.update(design_id, design)

    def delete(self, design_id: int) -> None:
        self._design_repository.delete(design_id)
