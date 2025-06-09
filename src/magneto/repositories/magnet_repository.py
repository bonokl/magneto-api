from typing import List

from src.entities.magnet import Magnet

magnets: List[Magnet] = [
    Magnet(
        id=1,
        shape="Bar",
        multipole=True,
        magnet_geometry_default={"magnet_length_x_dim": 4, "magnet_length_y_dim": 4, "magnet_length_z_dim": 4},
        description="Commonly used in:\n Laptop lid closure\n Limit detection",
        magnet_image="http://webench.ti.com/media/images/magnets/bar.png",
        created_at=None,
        updated_at=None
    ),
    Magnet(
        id=2,
        shape="Diametric Cylinder",
        multipole=False,
        magnet_geometry_default={"outer_diameter": 3, "height": 6},
        description="Commonly used in:\n Angle Measurements\n End of Shaft Motor speed",
        magnet_image="http://webench.ti.com/media/images/magnets/diametric_cylinder.png",
        created_at=None,
        updated_at=None
    ),
    Magnet(
        id=3,
        shape="Axial Cylinder",
        multipole=False,
        magnet_geometry_default={"outer_diameter": 3, "height": 6},
        description="Commonly used in:\n Trigger detection\n Joystick\n Slide-By",
        magnet_image="http://webench.ti.com/media/images/magnets/axial_cylinder.png",
        created_at=None,
        updated_at=None
    ),
    Magnet(
        id=4,
        shape="Ring",
        multipole=True,
        magnet_geometry_default={"outer_diameter": 5, "inner_diameter": 3, "height": 6},
        description="Commonly used in:\n Angle Measurements\n On Shaft motor speed",
        magnet_image="http://webench.ti.com/media/images/magnets/ring.png",
        created_at=None,
        updated_at=None
    ),
    Magnet(
        id=5,
        shape="Axial Ring",
        multipole=True,
        magnet_geometry_default={"outer_diameter": 5, "inner_diameter": 3, "height": 6},
        description="Commonly used in:\n Angular Incremental Encoding",
        magnet_image="http://webench.ti.com/media/images/magnets/axial_ring.png",
        created_at=None,
        updated_at=None
    ),
    Magnet(
        id=6,
        shape="Sphere",
        multipole=False,
        magnet_geometry_default={"diameter": 6},
        description="Spherical magnets field contour is closest to an ideal magnetic dipole",
        magnet_image="http://webench.ti.com/media/images/magnets/sphere.png",
        created_at=None,
        updated_at=None
    ),
]


class MagnetRepository:
    def get(self, magnet_id: int) -> Magnet | None:
        for m in magnets:
            if m.id == magnet_id:
                return m
        return None

    def get_all(self) -> List[Magnet]:
        return magnets
