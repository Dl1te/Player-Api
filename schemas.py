from pydantic import BaseModel
from typing import Optional

class PlayerCreate(BaseModel):
    nick: str
    name: str
    donate: str = "0"

class PlayerUpdate(BaseModel):
    name: Optional[str] = None
    donate: Optional[str] = None

class PlayerResponse(BaseModel):
    id: int
    nick: str
    name: str
    donate: str
    
    class Config:
        from_attributes = True