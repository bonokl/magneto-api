from src.magneto.interfaces.design_interface import DesignInterface
from src.magneto.repositories.design_repository import DesignRepository
from src.entities.design import Design, CreateDesign, UpdateDesign
from typing import List, Optional, Tuple

class DesignService(DesignInterface):
    def __init__(self, design_repository: DesignRepository):
        self._design_repository = design_repository

    def get_all_designs(self, offset: int = 0, limit: int = 100, order_by: Optional[str] = None) -> Tuple[int, List[Design]]:
        return self._design_repository.get_all(offset, limit, order_by)

    def create_design(self, design: CreateDesign) -> Design:
        return self._design_repository.create(design)

    def update_design(self, design_id: int, design: UpdateDesign) -> Design | None:
        return self._design_repository.update(design_id, design)

    def get_design(self, design_id: int) -> Design | None:
        return self._design_repository.get(design_id)

    def delete_design(self, design_id: int) -> bool:
        return self._design_repository.delete(design_id)
