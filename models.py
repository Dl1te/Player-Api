from sqlalchemy import Column, Integer, String
from database import Base

class Player(Base):
    __tablename__ = "players"
    
    id = Column(Integer, primary_key=True, index=True)
    nick = Column(String, unique=True, index=True)
    name = Column(String)
    donate = Column(String, default="0")