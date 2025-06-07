from src.entities.function import Function
from typing import List

functions = [
            Function(
                id=1,
                name="Hinge",
                description=None,
                function_type="Hinge",
                magnet_movement_default={"arc_length": 30},
                sim_setting_default={"angular_step_size": 1},
                function_image="http://webench.ti.com/media/images/functions/hinge.png"
            ),
            Function(
                id=2,
                name="Linear",
                description=None,
                function_type="Linear",
                magnet_movement_default={"final_x_position": 10, "final_y_position": 0, "final_z_position": 0},
                sim_setting_default={"step_size": 1},
                function_image="http://webench.ti.com/media/images/functions/linear.png"
            ),
            Function(
                id=3,
                name="Joystick",
                description=None,
                function_type="Joystick",
                magnet_movement_default={"tilt_angle": 30, "xy_angle": 0},
                sim_setting_default={"tilt_angle_step_size": 1},
                function_image="http://webench.ti.com/media/images/functions/joystick.png"
            ),
            Function(
                id=4,
                name="Rotation",
                description=None,
                function_type="Rotation",
                magnet_movement_default={"arc_length": 360},
                sim_setting_default={"angular_step_size": 1},
                function_image="http://webench.ti.com/media/images/functions/rotation.png"
            ),
            Function(
                id=5,
                name="Static Position",
                description=None,
                function_type="Static Position",
                magnet_movement_default={},
                sim_setting_default={},
                function_image="http://webench.ti.com/media/images/functions/discrete.svg"
            ),
        ]

class FunctionRepository:
    def get(self, function_id: int) -> Function | None:
        for f in functions:
            if f.id == function_id:
                return f
        return None

    def get_all(self) -> List[Function]:
        return functions
