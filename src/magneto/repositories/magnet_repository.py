from typing import List

from src.entities.magnet import Magnet, MagnetGeometry, MagnetShape

magnets: List[Magnet] = [
    Magnet(
        id=1,
        shape=MagnetShape.BAR,
        multipole=True,
        magnet_geometry_default=MagnetGeometry(
            magnet_length_x=40,
            magnet_length_y=40,
            magnet_length_z=40
        ),
        description=""
    )
]


class MagnetRepository:
    def get(self, magnet_id: int) -> Magnet | None:
        for m in magnets:
            if m.id == magnet_id:
                return m
        return None

    def get_all(self) -> List[Magnet]:
        return magnets
