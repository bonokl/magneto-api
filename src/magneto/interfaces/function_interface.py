from abc import ABC, abstractmethod

from src.entities.function import Function


class FunctionInterface(ABC):
    @abstractmethod
    def get_all_functions(self) -> list[Function]:
        pass

    @abstractmethod
    def get_function(self, function_id: int) -> Function | None:
        pass
