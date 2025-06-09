from src.entities.function import Function, FunctionType

functions = [
    Function(
        id=5,
        name="Static Position",
        function_type=FunctionType.static,
    )
]


class FunctionRepository:
    def get(self, function_id: int) -> Function | None:
        for f in functions:
            if f.id == function_id:
                return f
        return None

    def get_all(self) -> list[Function]:
        return functions
