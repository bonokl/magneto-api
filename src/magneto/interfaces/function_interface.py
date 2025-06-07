from abc import ABC, abstractmethod
from typing import List, Optional
from src.entities.function import Function

class FunctionInterface(ABC):
    @abstractmethod
    def get_all_functions(self) -> List[Function]:
        pass

    @abstractmethod
    def get_function(self, function_id: int) -> Function | None:
        pass


