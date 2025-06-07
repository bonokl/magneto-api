from threading import Lock
from typing import List, Optional, Tuple

from src.entities.design import CreateDesign, Design, UpdateDesign

# In-memory storage for designs
designs_store = {}
designs_lock = Lock()


class DesignRepository:
    def get(self, design_id: int) -> Design | None:
        with designs_lock:
            return designs_store.get(design_id)

    def get_all(self, offset: int = 0, limit: int = 100, order_by: Optional[str] = None) -> Tuple[int, List[Design]]:
        with designs_lock:
            designs = list(designs_store.values())
            if order_by == 'name':
                designs.sort(key=lambda d: d.name)
            elif order_by == 'name_desc':
                designs.sort(key=lambda d: d.name, reverse=True)
            count = len(designs)
            return count, designs[offset:offset + limit]

    def create(self, design: CreateDesign) -> Design:
        with designs_lock:
            new_id = max(designs_store.keys(), default=0) + 1
            new_design = Design(id=new_id, **design.model_dump())
            designs_store[new_id] = new_design
            return new_design

    def update(self, design_id: int, design: UpdateDesign) -> Design | None:
        with designs_lock:
            if design_id not in designs_store:
                return None
            update_data = design.model_dump(exclude_unset=True)
            current = designs_store[design_id].model_copy(update=update_data)
            designs_store[design_id] = current
            return current

    def delete(self, design_id: int) -> bool:
        with designs_lock:
            if design_id in designs_store:
                del designs_store[design_id]
                return True
            return False
