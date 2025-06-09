from src.entities.function import Function
from src.magneto.interfaces.function_interface import FunctionInterface
from src.magneto.repositories.function_repository import FunctionRepository


class FunctionService(FunctionInterface):
    def __init__(self, function_repository: FunctionRepository):
        self._function_repository = function_repository

    def get_all_functions(self) -> list[Function]:
        return self._function_repository.get_all()

    def get_function(self, function_id: int) -> Function | None:
        return self._function_repository.get(function_id)
