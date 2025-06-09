from src.entities.magnet_material import MagnetMaterial, MaterialGrade

magnet_materials = [
    MagnetMaterial(id=1, name="NdFeB", description="Neodymium Iron Boron")
]
material_grades = [
    MaterialGrade(id=1, material_id=1, grade="N35", br_low=1180, br_average=1200, br_high=1220,
                  temperature_coefficient=-0.12, coercivity=10.9, description=None),
    MaterialGrade(id=2, material_id=1, grade="N38", br_low=1220, br_average=1240, br_high=1260,
                  temperature_coefficient=-0.12, coercivity=11.3, description=None),
    MaterialGrade(id=3, material_id=1, grade="N40", br_low=1260, br_average=1275, br_high=1290,
                  temperature_coefficient=-0.12, coercivity=11.4, description=None),
    MaterialGrade(id=4, material_id=1, grade="N42", br_low=1290, br_average=1310, br_high=1330,
                  temperature_coefficient=-0.12, coercivity=11.5, description=None),
    MaterialGrade(id=5, material_id=1, grade="N45", br_low=1330, br_average=1350, br_high=1370,
                  temperature_coefficient=-0.12, coercivity=11, description=None),
    MaterialGrade(id=6, material_id=1, grade="N48", br_low=1370, br_average=1390, br_high=1410,
                  temperature_coefficient=-0.12, coercivity=10.5, description=None),
    MaterialGrade(id=7, material_id=1, grade="N50", br_low=1400, br_average=1425, br_high=1450,
                  temperature_coefficient=-0.12, coercivity=10.5, description=None),
    MaterialGrade(id=8, material_id=1, grade="N52", br_low=1430, br_average=1455, br_high=1480,
                  temperature_coefficient=-0.12, coercivity=10.5, description=None),
    MaterialGrade(id=9, material_id=1, grade="N55", br_low=1470, br_average=1490, br_high=1510,
                  temperature_coefficient=-0.12, coercivity=10.5, description=None),
]


class MagnetMaterialRepository:
    def get_all_magnet_materials(self) -> list[MagnetMaterial]:
        return magnet_materials

    def get_all_material_grades(self, magnet_material_id: int) -> list[MaterialGrade]:
        return [grade for grade in material_grades if grade.material_id == magnet_material_id]
