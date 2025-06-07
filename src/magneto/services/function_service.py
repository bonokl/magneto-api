from src.magneto.interfaces.function_interface import FunctionInterface
from src.magneto.repositories.function_repository import FunctionRepository
from src.entities.function import Function
from typing import List, Optional, Tuple

class FunctionService(FunctionInterface):
    def __init__(self, function_repository: FunctionRepository):
        self._function_repository = function_repository

    def get_all_functions(self) -> List[Function]:
        return self._function_repository.get_all()

    def get_function(self, function_id: int) -> Function | None:
        return self._function_repository.get(function_id)

