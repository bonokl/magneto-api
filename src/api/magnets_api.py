from src.entities.magnet import Magnet
from src.entities.pagination import Metadata, Paginated
from src.magneto import container


async def get_all_magnets() -> Paginated[Magnet]:
    functions = container.magnets.get_all_magnets()
    metadata = Metadata(count=1, page=1, size=1, sort="id")
    paginated = Paginated[Magnet](data=functions, metadata=metadata)
    return paginated


async def get_magnet(magnet_id: int) -> Magnet:
    return container.magnets.get_magnet(magnet_id)
