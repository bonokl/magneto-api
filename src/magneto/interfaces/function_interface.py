from abc import ABC, abstractmethod
from typing import List, Optional
from src.entities.function import Function

class FunctionInterface(ABC):
    @abstractmethod
    def get_all_functions(self, offset: int = 0, limit: int = 100, order_by: Optional[str] = None) -> (int, List[Function]):
        pass

    @abstractmethod
    def create_function(self, name: str, description: Optional[str] = None) -> Function:
        pass

    @abstractmethod
    def update_function(self, function_id: int, name: Optional[str] = None, description: Optional[str] = None) -> Function | None:
        pass

    @abstractmethod
    def get_function(self, function_id: int) -> Function | None:
        pass

    @abstractmethod
    def delete_function(self, function_id: int) -> bool:
        pass

