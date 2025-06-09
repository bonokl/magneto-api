from pydantic import BaseModel


class Metadata(BaseModel):
    count: int
    page: int
    size: int
    sort: str


class Paginated[T](BaseModel):
    data: list[T]
    metadata: Metadata
