from src.entities.magnet_material import MagnetMaterial, MaterialGrade
from src.entities.pagination import Metadata, Paginated
from src.magneto import container


async def get_all_magnet_materials() -> Paginated[MagnetMaterial]:
    magnet_materials = container.magnet_materials.get_all_magnet_materials()
    metadata = Metadata(count=1, page=1, size=1, sort="id")
    paginated = Paginated[MagnetMaterial](data=magnet_materials, metadata=metadata)
    return paginated


async def get_all_material_grades(material_id: int) -> Paginated[MaterialGrade]:
    grades = container.magnet_materials.get_all_material_grades(material_id)
    metadata = Metadata(count=1, page=1, size=1, sort="id")
    paginated = Paginated[MaterialGrade](data=grades, metadata=metadata)
    return paginated
