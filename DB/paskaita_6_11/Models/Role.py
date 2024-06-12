from sqlalchemy import Column, ForeignKey, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from Models.associations import role_user_associasion


class Role(Base):
    __tablename__ = 'Roles'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    users = relationship("Users", secondary= role_user_associasion , back_populates= "Roles")
    
    
    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return f"{self.id}|{self.name}"