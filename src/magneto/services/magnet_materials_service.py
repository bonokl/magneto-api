from src.entities.magnet_material import MagnetMaterial, MaterialGrade
from src.magneto.interfaces.magnet_materials_interface import MagnetMaterialsInterface
from src.magneto.repositories.magnet_material_repository import MagnetMaterialRepository


class MagnetMaterialsService(MagnetMaterialsInterface):
    def __init__(self, magnet_material_repository: MagnetMaterialRepository):
        self.magnet_material_repository = magnet_material_repository

    def get_all_magnet_materials(self) -> list[MagnetMaterial]:
        return self.magnet_material_repository.get_all_magnet_materials()

    def get_all_material_grades(self, magnet_material_id: int) -> list[MaterialGrade]:
        return self.magnet_material_repository.get_all_material_grades(magnet_material_id)
