from pydantic import BaseModel, Field
from datetime import datetime                                                                                         
from typing import Optional

class SpaceStation(BaseModel):
	station_id: str = Field(min_length=3, max_length=10)
	name: str = Field(min_length=1, max_length=50)
	crew_size: int = Field(ge=1, le=20)
	power_level: float = Field(ge=0.0, le=100.0)
	oxygen_level: float = Field(ge=0.0, le=100.0)
	last_maintenance: datetime = Field(default= datetime(2026, 1, 1))
	is_operational: bool = Field(default=True)
	notes: Optional[str] = Field(max_length=200)