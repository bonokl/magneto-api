from sqlalchemy import Boolean, Column, DateTime, Integer, JSON, String, Text, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Magnet(Base):
    __tablename__ = 'magnets'

    id = Column(Integer, primary_key=True, index=True)
    shape = Column(String, nullable=False)
    multipole = Column(Boolean, nullable=False)
    magnet_geometry_default = Column(JSON, nullable=False, default={})
    description = Column(Text, nullable=True)
    magnet_image = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
