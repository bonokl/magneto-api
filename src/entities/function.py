from typing import Any, Dict, Optional

from pydantic import BaseModel, Field


class Function(BaseModel):
    id: int
    name: str = Field(..., min_length=1, max_length=128)
    description: Optional[str] = None
    function_type: str
    magnet_movement_default: Dict[str, Any] = Field(default_factory=dict)
    sim_setting_default: Dict[str, Any] = Field(default_factory=dict)
    function_image: str

    class Config:
        from_attributes = True
