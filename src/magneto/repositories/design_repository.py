from typing import Dict, List, Optional

from src.entities.design import CreateDesign, Design, MagnetAngle, MagnetMovement, MagnetPosition, RemanenceType, \
    SimSetting
from src.entities.magnet import MagnetGeometry

default_design = Design(
    id=1,
    design_name="first",
    magnet_id=1,
    poles=2,
    material_id=1,
    grade_id=1,
    select_remanence=RemanenceType.BR_AVERAGE,
    remanence=1180,
    temperature=20,
    temperature_coefficient=-0.12,
    coercivity=10.9,
    function_id=5,
    magnet_geometry=MagnetGeometry(
        magnet_length_x=4,
        magnet_length_y=4,
        magnet_length_z=4
    ),
    magnet_position=MagnetPosition(
        x_position=0,
        y_position=0,
        z_position=0
    ),
    magnet_angle=MagnetAngle(
        x_angle=45,
        y_angle=0,
        z_angle=0
    ),
    magnet_movement=MagnetMovement(),
    sim_setting=SimSetting(),
    date_created="string",
    last_modified="string",
    sensor=[]
)


class DesignRepository:
    def __init__(self):
        self._data: Dict[int, Design] = {1: default_design}
        self._id_counter = 2

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
