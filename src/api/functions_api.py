from src.entities.function import Function
from src.entities.pagination import Metadata, Paginated
from src.magneto import container


async def get_all_functions() -> Paginated[Function]:
    functions = container.functions.get_all_functions()
    metadata = Metadata(count=1, page=1, size=1, sort="id")
    paginated = Paginated[Function](data=functions, metadata=metadata)
    return paginated


async def get_function(function_id: int) -> Function:
    return container.functions.get_function(function_id)
