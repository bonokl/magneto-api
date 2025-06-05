from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Magnet(Base):
    __tablename__ = 'magnets'

    id = Column(Integer, primary_key=True, index=True)
    design_id = Column(Integer, ForeignKey('designs.id'), nullable=False)
    name = Column(String, nullable=False)
    function_type = Column(String, nullable=False)  # e.g., 'hinge', 'linear', 'rotation'
    shape_type = Column(String, nullable=False)     # e.g., 'bar', 'ring'
    parameters = Column(JSON, nullable=False)       # shape-specific parameters
    position = Column(JSON, nullable=False)         # initial position/orientation
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

