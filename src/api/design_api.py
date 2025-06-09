from fastapi import HTTPException, status

from src.entities.design import CreateDesign, Design
from src.entities.pagination import Metadata, Paginated
from src.magneto import container


async def get_all_designs() -> Paginated[Design]:
    designs = container.designs.get_all()
    metadata = Metadata(count=len(designs), page=1, size=len(designs), sort="id")
    paginated = Paginated[Design](data=designs, metadata=metadata)
    return paginated


async def get_design(design_id: int) -> Design:
    design = container.designs.get(design_id)
    if design is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="not found")
    return design


async def create_design(design: CreateDesign) -> Design:
    created = container.designs.create(design)
    return created


async def update_design(design_id: int, design: CreateDesign) -> Design:
    updated = container.designs.update(design_id, design)
    if updated is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="not found")
    return updated


async def delete_design(design_id: int) -> None:
    deleted = container.designs.delete(design_id)
    if deleted is False:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="not found")
