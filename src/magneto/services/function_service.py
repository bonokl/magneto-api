from src.magneto.interfaces.function_interface import FunctionInterface
from src.magneto.repositories.function_repository import FunctionRepository
from src.entities.function import Function
from typing import List, Optional, Tuple

class FunctionService(FunctionInterface):
    def __init__(self, function_repository: FunctionRepository):
        self._function_repository = function_repository

    def get_all_functions(self, offset: int = 0, limit: int = 100, order_by: Optional[str] = None) -> Tuple[int, List[Function]]:
        return self._function_repository.get_all(offset, limit, order_by)

    def create_function(self, name: str, description: Optional[str] = None) -> Function:
        return self._function_repository.create(name, description)

    def update_function(self, function_id: int, name: Optional[str] = None, description: Optional[str] = None) -> Function | None:
        # Update not implemented in repository, add if needed
        pass

    def get_function(self, function_id: int) -> Function | None:
        return self._function_repository.get(function_id)

    def delete_function(self, function_id: int) -> bool:
        return self._function_repository.delete(function_id)
