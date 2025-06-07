import magpylib as magpy
import numpy as np
from scipy.spatial.transform import Rotation as R

from src.entities.simulation_config import SimulationStartRequest
from src.magneto.interfaces.simulation_config_interface import SimulationConfigInterface
from src.magneto.repositories.simulation_config_repository import SimulationConfigRepository


class SimulationConfigService(SimulationConfigInterface):
    def __init__(self, simulation_config_repository: SimulationConfigRepository):
        self._simulation_config_repository = simulation_config_repository

    def start_simulation(self, sim_req: SimulationStartRequest) -> dict:
        result = {
            "status": "started",
            "message": "Simulation started successfully."
        }

        # Use sim_req for all simulation logic, using attributes directly
        geom = sim_req.magnet_geometry
        angle = sim_req.magnet_angle
        position = sim_req.magnet_position
        movement = sim_req.magnet_movement
        sensors = sim_req.sensor or []

        # Determine magnet type and create magnet
        if geom and geom.magnet_length_x_dim is not None and geom.magnet_length_y_dim is not None and geom.magnet_length_z_dim is not None:
            dimension = (
                geom.magnet_length_x_dim / 1000.0,
                geom.magnet_length_y_dim / 1000.0,
                geom.magnet_length_z_dim / 1000.0,
            )
            polarization = (sim_req.remanence / 1000.0, 0, 0)
            magnet = magpy.magnet.Cuboid(polarization=polarization, dimension=dimension)
        elif geom and geom.outer_diameter is not None and geom.height is not None:
            dimension = (geom.outer_diameter / 1000.0, geom.height / 1000.0)
            polarization = (sim_req.remanence / 1000.0, 0, 0)
            magnet = magpy.magnet.Cylinder(polarization=polarization, dimension=dimension)
        else:
            raise ValueError("Unsupported magnet geometry for simulation.")

        # Set magnet position and orientation
        magnet.position = (
            (position.x_position if position and position.x_position is not None else 0) / 1000.0,
            (position.y_position if position and position.y_position is not None else 0) / 1000.0,
            (position.z_position if position and position.z_position is not None else 0) / 1000.0,
        )
        magnet.orientation = R.from_euler(
            'xyz',
            [
                angle.x_angle if angle and angle.x_angle is not None else 0,
                angle.y_angle if angle and angle.y_angle is not None else 0,
                angle.z_angle if angle and angle.z_angle is not None else 0,
            ],
            degrees=True
        )

        # Handle magnet movement (e.g., arc_length, final position)
        if movement and movement.arc_length is not None:
            arc = movement.arc_length
            angles = np.linspace(0, arc, 10)
            positions = []
            for a in angles:
                magnet.orientation = R.from_euler('z', a, degrees=True)
                positions.append(magnet.orientation.as_rotvec(degrees=True))

        # Create sensors and set their positions/orientations
        magpy_sensors = []
        for s in sensors:
            sensor = magpy.Sensor()
            spos = s.sensor_position
            sensor.position = (
                (spos.x_position if spos and spos.x_position is not None else 0) / 1000.0,
                (spos.y_position if spos and spos.y_position is not None else 0) / 1000.0,
                (spos.z_position if spos and spos.z_position is not None else 0) / 1000.0,
            )
            sangle = s.sensor_angle
            sensor.orientation = R.from_euler(
                'xyz',
                [
                    sangle.x_angle if sangle and sangle.x_angle is not None else 0,
                    sangle.y_angle if sangle and sangle.y_angle is not None else 0,
                    sangle.z_angle if sangle and sangle.z_angle is not None else 0,
                ],
                degrees=True
            )
            magpy_sensors.append(sensor)

        # Compute B-field at each sensor
        B_fields = []
        for sensor in magpy_sensors:
            B = magpy.getB(magnet, sensor)
            B_fields.append(B.tolist())

        # Prepare output in required structure
        # Map function_id to function name (for demo, hardcoded)
        function_map = {
            1: "Rotation",
            2: "Linear",
            3: "Joystick",
            4: "Hinge",
            5: "Static Position"
        }
        function_name = function_map.get(sim_req.function_id, str(sim_req.function_id))
        result = {
            "magnet_animation": {
                "function": function_name,
                # Add more animation data as needed
            },
            "graphs": {
                "data": {
                    -1: {
                        "magnet_field_distance_graph": {
                            "plots": [
                                {"B_field": B_fields, "label": "B-field at sensors"}
                            ],
                            "metadata": {
                                "unit": "T",
                                "description": "Magnetic field at sensor positions"
                            }
                        }
                    }
                },
                "metadata": {
                    "simulation": "Magneto",
                    "sensors": len(magpy_sensors)
                }
            }
        }
        return result
