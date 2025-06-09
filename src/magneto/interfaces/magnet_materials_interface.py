from abc import ABC, abstractmethod

from src.entities.magnet_material import MagnetMaterial, MaterialGrade


class MagnetMaterialsInterface(ABC):

    @abstractmethod
    def get_all_magnet_materials(self) -> list[MagnetMaterial]:
        pass

    @abstractmethod
    def get_all_material_grades(self, magnet_material_id: int) -> list[MaterialGrade]:
        pass
