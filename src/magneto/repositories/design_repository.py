from typing import Dict, List, Optional

from src.entities.design import Design
from src.magneto.interfaces.design_interface import DesignInterface


class DesignRepository(DesignInterface):
    def __init__(self):
        self._data: Dict[int, Design] = {}
        self._id_counter = 1

    def get_all(self) -> List[Design]:
        return list(self._data.values())

    def get(self, design_id: int) -> Optional[Design]:
        return self._data.get(design_id)

    def create(self, design: Design) -> Design:
        design_id = self._id_counter
        self._id_counter += 1
        # Set the id if not present
        if hasattr(design, 'id'):
            setattr(design, 'id', design_id)
        self._data[design_id] = design
        return design

    def update(self, design_id: int, design: Design) -> Design:
        if design_id not in self._data:
            raise ValueError(f"Design with id {design_id} does not exist.")
        # Optionally update the id
        if hasattr(design, 'id'):
            setattr(design, 'id', design_id)
        self._data[design_id] = design
        return design

    def delete(self, design_id: int) -> None:
        if design_id in self._data:
            del self._data[design_id]
