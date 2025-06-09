from typing import Dict, List, Optional

from src.entities.design import CreateDesign, Design


class DesignRepository:
    def __init__(self):
        self._data: Dict[int, Design] = {}
        self._id_counter = 1

    def get_all(self) -> List[Design]:
        return list(self._data.values())

    def get(self, design_id: int) -> Optional[Design]:
        return self._data.get(design_id)

    def create(self, design: CreateDesign) -> Design:
        design_id = self._id_counter
        self._id_counter += 1
        # Map CreateDesign to Design and set the id
        design_data = design.model_dump()
        design_data['id'] = design_id
        new_design = Design(**design_data)
        self._data[design_id] = new_design
        return new_design

    def update(self, design_id: int, design: CreateDesign) -> Design:
        if design_id not in self._data:
            raise ValueError(f"Design with id {design_id} does not exist.")
        # Optionally update the id
        design_data = design.model_dump()
        design_data['id'] = design_id
        updated_design = Design(**design_data)

        self._data[design_id] = updated_design
        return updated_design

    def delete(self, design_id: int) -> None:
        if design_id in self._data:
            del self._data[design_id]
