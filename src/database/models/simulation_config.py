from sqlalchemy import Column, Integer, DateTime, ForeignKey, JSON, Float, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SimulationConfig(Base):
    __tablename__ = 'simulation_configs'

    id = Column(Integer, primary_key=True, index=True)
    design_id = Column(Integer, ForeignKey('designs.id'), nullable=False)
    step_size = Column(Float, nullable=False)
    start_point = Column(JSON, nullable=False)  # position/orientation
    end_point = Column(JSON, nullable=False)    # position/orientation
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

