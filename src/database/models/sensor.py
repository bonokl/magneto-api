from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Sensor(Base):
    __tablename__ = 'sensors'

    id = Column(Integer, primary_key=True, index=True)
    design_id = Column(Integer, ForeignKey('designs.id'), nullable=False)
    name = Column(String, nullable=False)
    sensor_type = Column(String, nullable=False)  # e.g., Hall, GMR, etc.
    parameters = Column(JSON, nullable=False)      # sensor-specific parameters
    position = Column(JSON, nullable=False)        # initial position/orientation
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

