from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship

Base = declarative_base()

# Association table for many-to-many relationship between Design and Sensor
DesignSensorAssociation = Table(
    'design_sensors', Base.metadata,
    Column('design_id', Integer, ForeignKey('designs.id'), primary_key=True),
    Column('sensor_id', Integer, ForeignKey('sensors.id'), primary_key=True)
)

class Design(Base):
    __tablename__ = 'designs'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    function_id = Column(Integer, nullable=False)
    magnet_id = Column(Integer, ForeignKey('magnets.id'), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    sensors = relationship('Sensor', secondary=DesignSensorAssociation, backref='designs')
