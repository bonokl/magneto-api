from pydantic import BaseModel


class Sensor(BaseModel):
    id: str
    name: str

    class Config:
        from_attributes = True
